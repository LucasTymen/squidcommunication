#!/usr/bin/env python3
"""Generate a new communication campaign skeleton.

Usage:
    python scripts/create_campaign.py 2025-12-ai-feuilleton \
        --platforms linkedin instagram \
        --posts 3 \
        --series "Saga SquidResearch" \
        --episode 1 \
        --start-date 2025-12-01
"""
from __future__ import annotations

import argparse
import json
import os
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, Iterable, List, Optional

SUPER_ADMIN_USERS = {"lucas"}


def ensure_super_admin() -> None:
    current_user = os.getenv("USER") or os.getenv("USERNAME") or "unknown"
    if current_user not in SUPER_ADMIN_USERS:
        raise SystemExit(
            "Accès réservé au super-admin. Merci d’exécuter ce script depuis le compte autorisé."
        )


ROOT = Path(__file__).resolve().parent.parent
CAMPAIGNS_DIR = ROOT / "campaigns"
TEMPLATES_DIR = ROOT / "templates"


@dataclass
class PlatformTemplate:
    platform: str
    subdir: str
    template_path: Path
    format: str
    filename_pattern: str
    default_type: str


PLATFORM_TEMPLATES: Dict[str, PlatformTemplate] = {
    "linkedin": PlatformTemplate(
        platform="linkedin",
        subdir="linkedin",
        template_path=TEMPLATES_DIR / "linkedin-post-simple.md",
        format="simple",
        filename_pattern="post-{index:02d}.md",
        default_type="post",
    ),
    "instagram": PlatformTemplate(
        platform="instagram",
        subdir="instagram",
        template_path=TEMPLATES_DIR / "instagram-story.md",
        format="story",
        filename_pattern="story-{index:02d}.md",
        default_type="story",
    ),
    "twitter": PlatformTemplate(
        platform="twitter",
        subdir="twitter",
        template_path=TEMPLATES_DIR / "twitter" / "thread.md",
        format="thread",
        filename_pattern="thread-{index:02d}.md",
        default_type="thread",
    ),
    "threads": PlatformTemplate(
        platform="threads",
        subdir="threads",
        template_path=TEMPLATES_DIR / "threads" / "thread.md",
        format="thread",
        filename_pattern="thread-{index:02d}.md",
        default_type="thread",
    ),
    "bluesky": PlatformTemplate(
        platform="bluesky",
        subdir="bluesky",
        template_path=TEMPLATES_DIR / "bluesky" / "post.md",
        format="post",
        filename_pattern="post-{index:02d}.md",
        default_type="post",
    ),
}


def parse_args(argv: Optional[Iterable[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate a new communication campaign")
    parser.add_argument("slug", help="Campaign slug (ex: 2025-12-ai-feuilleton)")
    parser.add_argument(
        "--platforms",
        nargs="+",
        default=["linkedin"],
        help="List of platforms to generate (default: linkedin)",
    )
    parser.add_argument(
        "--posts",
        type=int,
        default=3,
        help="Number of posts per platform (default: 3)",
    )
    parser.add_argument(
        "--start-date",
        dest="start_date",
        default=datetime.utcnow().strftime("%Y-%m-%d"),
        help="Start date for scheduling (YYYY-MM-DD)",
    )
    parser.add_argument("--objective", default="", help="High level objective for the campaign")
    parser.add_argument("--cta", default="", help="Primary call-to-action")
    parser.add_argument("--angle", default="storytelling", help="Content angle (storytelling/data/tech)")
    parser.add_argument("--series", default=None, help="Narrative series name (optional)")
    parser.add_argument("--episode", type=int, default=None, help="Episode number in the series")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Simulate the creation without writing files",
    )
    return parser.parse_args(argv)


def validate_platforms(platforms: List[str]) -> List[PlatformTemplate]:
    resolved = []
    for platform in platforms:
        key = platform.lower()
        if key not in PLATFORM_TEMPLATES:
            raise ValueError(f"Unsupported platform '{platform}'. Available: {', '.join(PLATFORM_TEMPLATES.keys())}")
        resolved.append(PLATFORM_TEMPLATES[key])
    return resolved


def ensure_directory(path: Path, dry_run: bool = False) -> None:
    if path.exists():
        return
    if dry_run:
        print(f"[DRY-RUN] mkdir {path}")
    else:
        path.mkdir(parents=True, exist_ok=True)


def load_template(path: Path) -> str:
    if not path.exists():
        return "# Draft\n\nTODO: write content"
    return path.read_text(encoding="utf-8")


def fill_template(content: str, context: Dict[str, str]) -> str:
    for key, value in context.items():
        placeholder = f"{{{{{key}}}}}"
        content = content.replace(placeholder, value)
    return content


def iso_now() -> str:
    return datetime.utcnow().replace(microsecond=0).isoformat() + "Z"


def schedule_dates(start_date: str, count: int, step_days: int = 2) -> List[str]:
    base = datetime.strptime(start_date, "%Y-%m-%d")
    return [
        (base + timedelta(days=index * step_days)).strftime("%Y-%m-%dT10:00:00Z")
        for index in range(count)
    ]


def build_campaign_json(
    slug: str,
    platforms: List[PlatformTemplate],
    posts: int,
    start_date: str,
    objective: str,
    cta: str,
    angle: str,
    series: Optional[str],
    episode: Optional[int],
) -> Dict:
    now = iso_now()
    schedule = schedule_dates(start_date, posts)
    posts_data = []
    for platform_tpl in platforms:
        for index, date in enumerate(schedule, start=1):
            posts_data.append(
                {
                    "post_id": f"{platform_tpl.platform}-{index:02d}",
                    "platform": platform_tpl.platform,
                    "format": platform_tpl.format,
                    "type": platform_tpl.default_type,
                    "status": "draft",
                    "template": str(platform_tpl.template_path.relative_to(ROOT)),
                    "scheduled_date": date,
                    "file": f"{platform_tpl.subdir}/{platform_tpl.filename_pattern.format(index=index)}",
                    "analytics": {
                        "impressions": 0,
                        "engagement": {"likes": 0, "comments": 0, "shares": 0},
                    },
                }
            )
    campaign: Dict[str, object] = {
        "schema_version": "1.0",
        "campaign_id": slug,
        "slug": slug.split("-", 2)[-1] if "-" in slug else slug,
        "created_at": now,
        "updated_at": now,
        "owner": "Lucas Tymen",
        "status": "draft",
        "objective": objective,
        "message_key": "",
        "platforms": [tpl.platform for tpl in platforms],
        "angle": angle,
        "kpis": {
            "target": {
                "linkedin_impressions": 0,
                "instagram_views": 0,
                "cta_clicks": 0,
            },
            "actual": {
                "linkedin_impressions": 0,
                "instagram_views": 0,
                "cta_clicks": 0,
            },
            "source": "manual",
        },
        "mcp_collaboration": {
            "calendar_event_id": "",
            "notion_template": "",
            "drive_folder": "",
            "tasks": [],
        },
        "content": {
            "summary": "",
            "angle": angle,
            "hashtags": [],
            "cta": cta,
            "assets": {
                "original": f"campaigns/{slug}/assets/original/",
                "sanitized": f"campaigns/{slug}/assets/sanitized/",
            },
        },
        "posts": posts_data,
        "security_checklist": {
            "no_ip_visible": False,
            "credentials_masked": False,
            "no_tokens": False,
            "client_data_anonymized": False,
            "internal_urls_masked": False,
            "env_vars_hidden": False,
            "validation_script_run": False,
            "validated_by": "",
            "validated_at": "",
        },
        "sync": {
            "source_repo": "squidResearch",
            "last_pulled": None,
            "last_pushed": None,
            "lock": False,
        },
        "notes": [],
    }
    if series:
        campaign["narrative_arc"] = {
            "episode": episode or 1,
            "series": series,
            "summary": "",
            "next_episode": "",
        }
    return campaign


def write_campaign(campaign_dir: Path, data: Dict, dry_run: bool = False) -> None:
    campaign_json_path = campaign_dir / "campaign.json"
    if dry_run:
        print(f"[DRY-RUN] would write {campaign_json_path}")
        print(json.dumps(data, indent=2, ensure_ascii=False))
        return
    with campaign_json_path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")


def create_post_files(
    campaign_dir: Path,
    platform_tpl: PlatformTemplate,
    posts: int,
    context: Dict[str, str],
    dry_run: bool = False,
) -> None:
    platform_dir = campaign_dir / platform_tpl.subdir
    ensure_directory(platform_dir, dry_run)
    template_content = load_template(platform_tpl.template_path)
    for index in range(1, posts + 1):
        filename = platform_tpl.filename_pattern.format(index=index)
        target_path = platform_dir / filename
        filled = fill_template(
            template_content,
            {
                **context,
                "POST_NUMBER": f"{index:02d}",
                "PUBLISH_AT": schedule_dates(context["START_DATE"], posts)[index - 1],
            },
        )
        if dry_run:
            print(f"[DRY-RUN] would write {target_path}")
            continue
        target_path.write_text(filled, encoding="utf-8")


def main() -> None:
    ensure_super_admin()
    args = parse_args()
    try:
        platforms = validate_platforms(args.platforms)
    except ValueError as exc:
        raise SystemExit(str(exc))

    campaign_dir = CAMPAIGNS_DIR / args.slug
    assets_original = campaign_dir / "assets" / "original"
    assets_sanitized = campaign_dir / "assets" / "sanitized"
    archive_dir = campaign_dir / "archive"

    for path in [campaign_dir, assets_original, assets_sanitized, archive_dir]:
        ensure_directory(path, args.dry_run)

    context = {
        "CAMPAIGN_ID": args.slug,
        "START_DATE": args.start_date,
    }

    campaign_data = build_campaign_json(
        slug=args.slug,
        platforms=platforms,
        posts=args.posts,
        start_date=args.start_date,
        objective=args.objective,
        cta=args.cta,
        angle=args.angle,
        series=args.series,
        episode=args.episode,
    )

    for tpl in platforms:
        create_post_files(campaign_dir, tpl, args.posts, context, args.dry_run)

    if not args.dry_run:
        write_campaign(campaign_dir, campaign_data, args.dry_run)
        # Create placeholder analytics file if absent
        analytics_path = archive_dir / "analytics.json"
        if not analytics_path.exists():
            analytics_path.write_text(json.dumps({"posts": []}, indent=2), encoding="utf-8")
        print(f"✅ Campaign '{args.slug}' generated at {campaign_dir}")
    else:
        print("[DRY-RUN] campaign generation simulated")


if __name__ == "__main__":
    main()
