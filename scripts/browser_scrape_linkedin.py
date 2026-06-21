import base64
import hashlib
import json
import os
import socket
import struct
import subprocess
import tempfile
import time
import urllib.request


EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"


class CDP:
    def __init__(self, url: str):
        self.sock = socket.create_connection((url.split("/")[2].split(":")[0], int(url.split("/")[2].split(":")[1])))
        key = base64.b64encode(os.urandom(16)).decode("ascii")
        path = "/" + "/".join(url.split("/")[3:])
        host = url.split("/")[2]
        request = (
            f"GET {path} HTTP/1.1\r\n"
            f"Host: {host}\r\n"
            "Upgrade: websocket\r\n"
            "Connection: Upgrade\r\n"
            f"Sec-WebSocket-Key: {key}\r\n"
            "Sec-WebSocket-Version: 13\r\n\r\n"
        )
        self.sock.sendall(request.encode("ascii"))
        response = self.sock.recv(4096)
        if b" 101 " not in response:
            raise RuntimeError(response.decode("latin1", "replace"))
        self.next_id = 0

    def _send_frame(self, payload: bytes) -> None:
        header = bytearray([0x81])
        length = len(payload)
        if length < 126:
            header.append(0x80 | length)
        elif length < 65536:
            header.append(0x80 | 126)
            header.extend(struct.pack("!H", length))
        else:
            header.append(0x80 | 127)
            header.extend(struct.pack("!Q", length))
        mask = os.urandom(4)
        header.extend(mask)
        masked = bytes(byte ^ mask[index % 4] for index, byte in enumerate(payload))
        self.sock.sendall(header + masked)

    def _read_exact(self, size: int) -> bytes:
        chunks = []
        remaining = size
        while remaining:
            chunk = self.sock.recv(remaining)
            if not chunk:
                raise RuntimeError("websocket closed")
            chunks.append(chunk)
            remaining -= len(chunk)
        return b"".join(chunks)

    def _recv_frame(self) -> dict:
        first, second = self._read_exact(2)
        length = second & 0x7F
        if length == 126:
            length = struct.unpack("!H", self._read_exact(2))[0]
        elif length == 127:
            length = struct.unpack("!Q", self._read_exact(8))[0]
        if second & 0x80:
            mask = self._read_exact(4)
            data = bytes(byte ^ mask[index % 4] for index, byte in enumerate(self._read_exact(length)))
        else:
            data = self._read_exact(length)
        if first & 0x0F == 8:
            raise RuntimeError("websocket closed")
        if first & 0x0F == 9:
            return self._recv_frame()
        return json.loads(data.decode("utf-8"))

    def call(self, method: str, params: dict | None = None, timeout: float = 30) -> dict:
        self.next_id += 1
        message_id = self.next_id
        self._send_frame(json.dumps({"id": message_id, "method": method, "params": params or {}}).encode("utf-8"))
        deadline = time.time() + timeout
        while time.time() < deadline:
            message = self._recv_frame()
            if message.get("id") == message_id:
                if "error" in message:
                    raise RuntimeError(message["error"])
                return message.get("result", {})
        raise TimeoutError(method)


def http_json(url: str) -> dict | list:
    with urllib.request.urlopen(url, timeout=10) as response:
        return json.loads(response.read().decode("utf-8"))


def launch_browser(port: int) -> subprocess.Popen:
    user_data_dir = tempfile.mkdtemp(prefix="codex-linkedin-edge-")
    return subprocess.Popen(
        [
            EDGE,
            "--headless=new",
            "--disable-gpu",
            "--no-sandbox",
            f"--remote-debugging-port={port}",
            f"--user-data-dir={user_data_dir}",
            "about:blank",
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


EXTRACT_JS = r"""
(() => {
  const clean = (text) => (text || '')
    .replace(/\u00a0/g, ' ')
    .replace(/[ \t]+\n/g, '\n')
    .replace(/\n{3,}/g, '\n\n')
    .trim();

  const mainArticle = [...document.querySelectorAll('article.main-feed-activity-card')]
    .find(article => !article.classList.contains('related-posts__crosslink'));
  const root = mainArticle || document;

  for (const button of [...root.querySelectorAll('button, [role="button"]')]) {
    const label = clean(button.innerText || button.getAttribute('aria-label'));
    if (/see more|show more|more$/i.test(label)) button.click();
  }

  const scripts = [...document.querySelectorAll('script[type="application/ld+json"]')];
  for (const script of scripts) {
    try {
      const data = JSON.parse(script.textContent);
      const items = Array.isArray(data) ? data : [data];
      for (const item of items) {
        if (item && item['@type'] === 'SocialMediaPosting') {
          const body = clean(item.articleBody || item.text);
          if (body) return body;
        }
      }
    } catch (_) {}
  }

  const commentary = root.querySelector('[data-test-id="main-feed-activity-card__commentary"], [data-test-id="main-feed-activity-card__commentary-expanded"]');
  const commentaryText = clean(commentary && (commentary.innerText || commentary.textContent)).replace(/\s*…more\s*$/i, '');
  const transcriptBlocks = [...root.querySelectorAll('section, div, p')]
    .map(node => clean(node.innerText || node.textContent))
    .filter(text => text.length > 200 && /^Transcript\b/i.test(text));
  const transcript = transcriptBlocks.sort((a, b) => b.length - a.length)[0] || '';
  if (commentaryText && transcript) return `${commentaryText}\n\n### Transcript\n\n${transcript.replace(/^Transcript\s+(Transcript\s*)?/i, '')}`;
  if (commentaryText) return commentaryText;

  const candidates = [...root.querySelectorAll('.feed-shared-update-v2__description-wrapper, .update-components-text, .feed-shared-inline-show-more-text, .break-words')]
    .map(node => clean(node.innerText || node.textContent))
    .filter(text => text.length > 40 && !/sign in|join linkedin|email or phone/i.test(text));
  if (candidates.length) {
    candidates.sort((a, b) => b.length - a.length);
    return candidates[0].replace(/\s*…more\s*$/i, '');
  }

  const meta = document.querySelector('meta[property="og:description"], meta[name="description"]');
  if (meta && meta.content) return clean(meta.content.split('|')[0]);
  return '';
})()
"""


def render_post(cdp: CDP, url: str) -> str:
    cdp.call("Page.navigate", {"url": url})
    time.sleep(8)
    cdp.call("Runtime.evaluate", {"expression": EXTRACT_JS, "awaitPromise": True})
    time.sleep(2)
    result = cdp.call("Runtime.evaluate", {"expression": EXTRACT_JS, "returnByValue": True, "awaitPromise": True})
    text = result.get("result", {}).get("value", "")
    return text.strip() if isinstance(text, str) else ""


class LinkedInBrowserScraper:
    def __init__(self) -> None:
        self.port = 9223 + (int(hashlib.sha1(str(time.time()).encode()).hexdigest(), 16) % 1000)
        self.browser: subprocess.Popen | None = None
        self.cdp: CDP | None = None

    def __enter__(self) -> "LinkedInBrowserScraper":
        self.browser = launch_browser(self.port)
        version_url = f"http://127.0.0.1:{self.port}/json/version"
        for _ in range(30):
            try:
                http_json(version_url)
                break
            except Exception:
                time.sleep(0.5)
        pages = http_json(f"http://127.0.0.1:{self.port}/json/list")
        page = next(item for item in pages if item.get("type") == "page")
        self.cdp = CDP(page["webSocketDebuggerUrl"])
        self.cdp.call("Page.enable")
        self.cdp.call("Runtime.enable")
        return self

    def __exit__(self, exc_type, exc, traceback) -> None:
        if self.browser:
            self.browser.terminate()

    def scrape_post_text(self, url: str) -> str:
        if not self.cdp:
            raise RuntimeError("Browser scraper has not been started")
        return render_post(self.cdp, url)


def main() -> None:
    from scrape_linkedin import main as scrape_main

    scrape_main()


if __name__ == "__main__":
    main()
