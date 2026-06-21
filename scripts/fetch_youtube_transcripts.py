import json
import re
import subprocess
import sys
import time
from pathlib import Path

import requests
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import (
    IpBlocked,
    NoTranscriptFound,
    RequestBlocked,
    TranscriptsDisabled,
    VideoUnavailable,
)

SCRIPT_DIR = Path(__file__).resolve().parent
BASE_DIR = SCRIPT_DIR.parent / "research" / "youtube-transcripts"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
}

youtube_targets = {
    "dan_petrovic": [
        {
            "title": "AI Search Mechanics | SEO Unplugged #37",
            "url": "https://youtu.be/jIKBAcGMNBs?si=ywErfEIw-Q-vhbn4",
        },
        {
            "title": "AI SEO Deep Dive",
            "url": "https://youtu.be/-f9QCqTqdTA?si=0ZgjmbU-0Q8RuGdZ",
        },
    ],
    "bernard_huang": [
        {
            "title": "How to Get Your Brand Cited by AI",
            "url": "https://youtu.be/mojvkc9CTWc?si=0svwJkIIBu7NMSn-",
        },
        {
            "title": "How Answer Engine Optimization (AEO) Works + Playbook",
            "url": "https://youtu.be/2Ldce9z_ZuM?si=CwDUM8aPJMkdSd9o",
        },
    ],
    "michal_suski": [
        {
            "title": "Learn How to Optimize for AI Search",
            "url": "https://www.youtube.com/live/OOepA6XL_-s?si=woffqx7y-ofJQd7M",
        },
        {
            "title": "AI Search Visibility Roast",
            "url": "https://www.youtube.com/live/MNVFjYIu5CU?si=kfk8-gHAm_k3Df1w",
        },
    ],
    "britney_muller": [
        {
            "title": "LLMs don't rank anything. So what are you optimizing for?",
            "url": "https://youtu.be/mJ8ipSF97AA?si=dDUFEvQuNhQam_Lu",
        },
        {
            "title": "What Marketers Get Wrong About ChatGPT",
            "url": "https://www.youtube.com/live/eznSG4kXt0E?si=LlPax1_7822hyNMO",
        },
    ],
    "eric_siu": [
        {
            "title": "How I Run a Marketing Agency With 6 AI Agents",
            "url": "https://youtu.be/WbRuIbRTeCM?si=X0jv5nMQLiyLmkaB",
        },
        {
            "title": "The SEO Playbook That Actually Works in 2026",
            "url": "https://youtu.be/UWHcOQCw4NU?si=9BFipGphPOmsEtMS",
        },
    ],
    "nathan_gotch": [
        {
            "title": "This is the #1 AI SEO ranking factor",
            "url": "https://youtu.be/mB0QuXEv_sg?si=HTjOkD0st8tmEiTt",
        },
        {
            "title": "How I'd Do SEO with AI in 2026",
            "url": "https://youtu.be/HkIu_gLJEdc?si=a89qjmwQM19V2s1b",
        },
    ],
    "koray_tugberk_gubur": [
        {
            "title": "AI & The Evolution Of SEO In 2026",
            "url": "https://youtu.be/EFPVohRjAgs?si=q-VVVhd4KN6vOzU0E",
        },
        {
            "title": "Master Semantic SEO & AI Agents",
            "url": "https://youtu.be/mSHq_HxOyTA?si=wScaVKV3yOvMIIq5",
        },
    ],
    "olga_zarr": [
        {
            "title": "AI and SEO in 2025 Masterclass",
            "url": "https://youtu.be/SruXYdccEVg?si=AhYcl_-UsOuEQaRn",
        },
        {
            "title": "How to Track AI Overviews",
            "url": "https://youtu.be/rMGKjwbnU3g?si=Ey4THyaz6VkxNNSN",
        },
    ],
    "lily_ray": [
        {
            "title": "AI Slop, GEO, and What Actually Works",
            "url": "https://youtu.be/DKAGf2lk488?si=dgwrY-FQ__nKmxpn",
        },
        {
            "title": "GEO, AEO, LLMO: Separating Fact from Fiction",
            "url": "https://youtu.be/2nJkT8zOzcM?si=RrVNNYA-L4gwBQCP",
        },
    ],
    "kevin_indig": [
        {
            "title": "The Great Decoupling & AI Driven Growth",
            "url": "https://youtu.be/p3_P0dDspBI?si=XKf2PGUnQ7-FGoP0",
        },
        {
            "title": "ChatGPT vs Google: The New Battleground",
            "url": "https://youtu.be/6Zm3wV3PhUc?si=WXZtGY1FfKap4ZvU",
        },
    ],
}


def extract_video_id(url: str) -> str:
    pattern = r"(?:v=|\/v\/|youtu\.be\/|\/embed\/|\/live\/)([a-zA-Z0-9_-]{11})"
    match = re.search(pattern, url)
    if not match:
        raise ValueError(f"Could not extract video ID from URL: {url}")
    return match.group(1)


def expert_slug(expert_key: str) -> str:
    return expert_key.replace("_", "-")


def sanitize_filename(title: str) -> str:
    cleaned = re.sub(r'[<>:"/\\|?*]', "-", title)
    cleaned = re.sub(r"\s+", " ", cleaned).strip(" .")
    return cleaned


def transcript_filename(title: str, video_id: str) -> str:
    return f"{sanitize_filename(title)} [{video_id}].md"


def webvtt_to_text(vtt: str) -> str:
    lines = []
    previous = None
    for raw_line in vtt.splitlines():
        line = raw_line.strip()
        if not line or line == "WEBVTT" or "-->" in line:
            continue
        if re.fullmatch(r"\d+", line):
            continue
        if line.startswith("NOTE"):
            continue
        if line != previous:
            lines.append(line)
            previous = line
    return "\n\n".join(lines)


def parse_srv3_xml(xml_text: str) -> str:
    import xml.etree.ElementTree as ET

    root = ET.fromstring(xml_text)
    lines = []
    for element in root.iter("text"):
        if element.text:
            lines.append(element.text.strip())
    return "\n\n".join(line for line in lines if line)


def fetch_via_timedtext(session: requests.Session, video_id: str) -> str:
    watch_url = f"https://www.youtube.com/watch?v={video_id}"
    response = session.get(watch_url, timeout=30)
    response.raise_for_status()

    match = re.search(r"ytInitialPlayerResponse\s*=\s*(\{.*?\});", response.text)
    if not match:
        raise RuntimeError("Could not parse YouTube player response")

    player = json.loads(match.group(1))
    captions = player.get("captions", {}).get("playerCaptionsTracklistRenderer", {})
    tracks = captions.get("captionTracks", [])
    if not tracks:
        raise RuntimeError("No caption tracks available")

    preferred = next((track for track in tracks if track.get("languageCode") == "en"), tracks[0])
    caption_url = preferred["baseUrl"]

    for suffix in ("&fmt=srv3", "&fmt=vtt", ""):
        caption_response = session.get(
            caption_url + suffix,
            headers={**HEADERS, "Referer": watch_url},
            timeout=30,
        )
        if caption_response.status_code == 429:
            continue
        caption_response.raise_for_status()
        body = caption_response.text.strip()
        if not body or body.startswith("<html"):
            continue
        if "WEBVTT" in body[:20] or "-->" in body:
            return webvtt_to_text(body)
        if body.startswith("<?xml") or body.startswith("<transcript"):
            return parse_srv3_xml(body)
        return body

    raise RuntimeError("Timedtext endpoint blocked or unavailable")


def fetch_via_transcript_api(session: requests.Session, video_id: str) -> str:
    api = YouTubeTranscriptApi(http_client=session)
    transcript = api.fetch(video_id, languages=("en", "en-US", "en-GB"))
    return "\n\n".join(snippet.text.strip() for snippet in transcript if snippet.text.strip())


def fetch_via_ytdlp(video_id: str) -> str:
    url = f"https://www.youtube.com/watch?v={video_id}"
    output_template = str(SCRIPT_DIR / f"_tmp_{video_id}")
    command = [
        "yt-dlp",
        "--write-auto-sub",
        "--write-sub",
        "--sub-lang",
        "en",
        "--skip-download",
        "--sub-format",
        "vtt",
        "--sleep-interval",
        "2",
        "-o",
        output_template,
        url,
    ]
    subprocess.run(command, check=True, capture_output=True, text=True)

    vtt_files = list(SCRIPT_DIR.glob(f"_tmp_{video_id}*.vtt"))
    if not vtt_files:
        raise RuntimeError("yt-dlp did not produce a subtitle file")

    text = webvtt_to_text(vtt_files[0].read_text(encoding="utf-8"))
    for vtt_file in vtt_files:
        vtt_file.unlink(missing_ok=True)
    return text


def fetch_transcript_text(video_id: str, session: requests.Session) -> str:
    errors = []

    for fetcher in (fetch_via_transcript_api, fetch_via_timedtext, fetch_via_ytdlp):
        try:
            if fetcher is fetch_via_ytdlp:
                return fetcher(video_id)
            return fetcher(session, video_id)
        except (IpBlocked, RequestBlocked, TranscriptsDisabled, NoTranscriptFound, VideoUnavailable, RuntimeError, subprocess.CalledProcessError) as error:
            errors.append(f"{fetcher.__name__}: {error}")

    raise RuntimeError("; ".join(errors))


def build_markdown(title: str, url: str, video_id: str, transcript_text: str) -> str:
    return (
        f"# Transcript: {title}\n"
        f"- **Source URL:** {url}\n"
        f"- **Video Identifier ID:** {video_id}\n\n"
        f"## Text Stream Logs\n\n{transcript_text.strip()}\n"
    )


def write_transcript_file(expert_key: str, video: dict, transcript_text: str) -> Path:
    video_id = extract_video_id(video["url"])
    expert_folder = BASE_DIR / expert_slug(expert_key)
    expert_folder.mkdir(parents=True, exist_ok=True)

    target_path = expert_folder / transcript_filename(video["title"], video_id)
    target_path.write_text(
        build_markdown(video["title"], video["url"], video_id, transcript_text),
        encoding="utf-8",
    )
    return target_path


def main() -> None:
    BASE_DIR.mkdir(parents=True, exist_ok=True)
    session = requests.Session()
    session.headers.update(HEADERS)

    total_videos = sum(len(videos) for videos in youtube_targets.values())
    print(f"Fetching transcripts for {total_videos} YouTube videos into {BASE_DIR}\n")

    failures = []
    written = 0

    for expert_key, videos in youtube_targets.items():
        print(f"{expert_slug(expert_key)}/")
        for index, video in enumerate(videos):
            video_id = extract_video_id(video["url"])
            print(f"  {video['title']} [{video_id}]")
            try:
                transcript_text = fetch_transcript_text(video_id, session)
                target_path = write_transcript_file(expert_key, video, transcript_text)
                print(f"    Wrote {target_path.relative_to(BASE_DIR.parent)} ({len(transcript_text)} chars)")
                written += 1
            except Exception as error:
                print(f"    FAILED: {error}")
                failures.append((video["url"], str(error)))
            if index < len(videos) - 1:
                time.sleep(2)

    print(f"\nDone. Wrote {written}/{total_videos} transcript files.")
    if failures:
        print("\nFailures:")
        for url, message in failures:
            print(f"  - {url}: {message}")
        sys.exit(1)


if __name__ == "__main__":
    main()
