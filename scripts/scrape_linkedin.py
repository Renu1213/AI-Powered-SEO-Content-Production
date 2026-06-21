import re
from pathlib import Path

from browser_scrape_linkedin import LinkedInBrowserScraper


SCRIPT_DIR = Path(__file__).resolve().parent
BASE_DIR = SCRIPT_DIR.parent / "research" / "linkedin-posts"

linkedin_targets = {
    "dan_petrovic": [
        {
            "title": "Past, Present, and Future of AI SEO (Part 1)",
            "url": "https://www.linkedin.com/posts/seoguy_1-past-present-and-future-of-ai-seo-2-activity-7407253126552092672-6CFY/",
        },
        {
            "title": "AI SEO Part 2: Model Attention & Primary Bias",
            "url": "https://www.linkedin.com/posts/seoguy_ai-seo-part-2-1-model-attention-primary-activity-7407534293498900481-uRN4/",
        },
        {
            "title": "AI SEO Part 3: Automated Citation Mining",
            "url": "https://www.linkedin.com/posts/seoguy_ai-seo-part-3-1-automated-citation-mining-activity-7407969688003104769-GvI2/",
        },
    ],
    "bernard_huang": [
        {
            "title": "When Kevin, Su, and I First Started Building",
            "url": "https://www.linkedin.com/posts/bernardjhuang_when-kevin-su-and-i-first-started-building-activity-7379157060388794368-2CyN/",
        },
    ],
    "britney_muller": [
        {
            "title": "AI Cheatsheet for Marketers 2026",
            "url": "https://www.linkedin.com/posts/britneymuller_ai-cheatsheet-for-marketers-2026-orange-labs-activity-7444766189719052288-2DND/",
        },
        {
            "title": "The AI Search Gold Rush: What's Real vs What's Hype",
            "url": "https://www.linkedin.com/posts/britneymuller_the-ai-search-gold-rush-whats-real-vs-whats-activity-7449472539904458752-TV7-/",
        },
    ],
    "eric_siu": [
        {
            "title": "There Are 3 Levels to How Teams Are Using AI",
            "url": "https://www.linkedin.com/posts/ericosiu_there-are-3-levels-to-how-teams-are-using-activity-7471958389653274624-z1ZE/",
        },
        {
            "title": "Highest Leverage Claude Code Dynamic Workflow",
            "url": "https://www.linkedin.com/posts/ericosiu_highest-leverage-claude-code-dynamic-workflow-activity-7466843524991401984-EPk1/",
        },
    ],
    "kevin_indig": [
        {
            "title": "Good Prompt Tracking Starts With Sample Design",
            "url": "https://www.linkedin.com/posts/kevinindig_good-prompt-tracking-starts-with-sample-design-activity-7470197035565002752-T8ow/",
        },
        {
            "title": "Two Brands Can Run Identical Optimization",
            "url": "https://www.linkedin.com/posts/kevinindig_two-brands-can-run-identical-on-page-optimization-activity-7473336241837731841-Dl3f/",
        },
    ],
    "koray_tugberk_gubur": [
        {
            "title": "Good News for SEOs: Google Is Bringing Generative AI",
            "url": "https://www.linkedin.com/posts/koray-tugberk-gubur_good-news-for-seos-google-is-bringing-generative-activity-7467874512357797888-FXPW/",
        },
    ],
    "lily_ray": [
        {
            "title": "Next Frontier of Spam Fighting",
            "url": "https://www.linkedin.com/posts/lily-ray-44755615_i-think-the-next-frontier-of-spam-fighting-share-7472261352552718336-kAj-/",
        },
        {
            "title": "The Worst Thing You Can Do for Your AI Search Strategy",
            "url": "https://www.linkedin.com/posts/lily-ray-44755615_the-worst-thing-you-can-do-for-your-ai-search-activity-7467554630458093568-81Xg/",
        },
    ],
    "michal_suski": [
        {
            "title": "This Blew My Mind: Did You Know You Can...",
            "url": "https://www.linkedin.com/posts/michal-suski_this-blew-my-mind-did-you-know-you-can-ugcPost-7270706278581116928-flXo/",
        },
    ],
    "nathan_gotch": [
        {
            "title": "AEO/GEO Is Just SEO - Watch This",
            "url": "https://www.linkedin.com/posts/nathangotch_aeogeo-is-just-seo-watch-this-activity-7472346313221656576-JFcM/",
        },
        {
            "title": "When Creating Pages for SEO/AEO",
            "url": "https://www.linkedin.com/posts/nathangotch_when-creating-pages-for-seo-aeo-they-activity-7457790873058291712-1MuE/",
        },
    ],
    "olga_zarr": [
        {
            "title": "AI and SEO in 2025: AI Optimization & SEO",
            "url": "https://www.linkedin.com/posts/olgazarr_ai-and-seo-in-2025-ai-optimization-seo-activity-7346816475539615744-Cung/",
        },
    ],
}


def slugify_author(author: str) -> str:
    return re.sub(r"-+", "-", author.replace("_", "-").lower()).strip("-")


def filename_for_title(title: str) -> str:
    filename = re.sub(r"[^\w\s-]", "", title, flags=re.ASCII)
    filename = re.sub(r"\s+", " ", filename).strip()
    return f"{filename or 'LinkedIn Post'}.md"


def build_post_markdown(author: str, post: dict, body: str) -> str:
    return (
        f"# LinkedIn Post: {post['title']}\n"
        f"- **Author:** {author.replace('_', ' ').title()}\n"
        f"- **Target Link:** {post['url']}\n\n"
        f"## Text Content\n\n{body.strip()}\n"
    )


def write_post(author: str, post: dict, body: str) -> Path:
    author_dir = BASE_DIR / slugify_author(author)
    author_dir.mkdir(parents=True, exist_ok=True)
    target_path = author_dir / filename_for_title(post["title"])
    target_path.write_text(build_post_markdown(author, post, body), encoding="utf-8")
    return target_path


def main() -> None:
    total_posts = sum(len(posts) for posts in linkedin_targets.values())
    BASE_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Scraping {total_posts} LinkedIn posts into {BASE_DIR}")

    written = []
    with LinkedInBrowserScraper() as scraper:
        for author, posts in linkedin_targets.items():
            print(f"\n{author}:")
            for post in posts:
                print(f"  Scraping: {post['title']}")
                body = scraper.scrape_post_text(post["url"]) or "[Could not extract post content]"
                out_file = write_post(author, post, body)
                written.append(out_file)
                print(f"  Wrote {out_file.relative_to(SCRIPT_DIR.parent)}")

    print(f"\nDone. Wrote {len(written)} files.")


if __name__ == "__main__":
    main()
