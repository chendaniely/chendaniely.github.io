"""Fetch my GitHub repos tagged `vibe-coded` into projects/vibe-coded.yml.

Runs as a Quarto pre-render script (see _quarto.yml), so every site build
pulls fresh repo metadata: tag a repo with the `vibe-coded` topic on GitHub
and it appears on projects/index.qmd at the next render.

Repos outside my account (e.g. ones living in an org I made for them) aren't
found by the topic search — pin those by hand in EXTRA_REPOS. Their card
details still come from GitHub, same as the tagged ones.

- Public repos only — a private repo tagged `vibe-coded` is skipped.
- Uses $GITHUB_TOKEN when present (CI) for higher rate limits;
  unauthenticated works fine for local builds.
- Locally, a file younger than an hour is reused so `quarto preview`
  doesn't hit the API on every re-render. CI always fetches.
- If the fetch fails, the previous file is kept (or an empty list is
  written) so a GitHub hiccup never breaks the build.

Standard library only — no requirements.txt changes needed.
"""

import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

USER = "chendaniely"
TOPIC = "vibe-coded"
# "owner/repo" for repos to list regardless of owner or topic
EXTRA_REPOS = [
    "pstrunners/pstrunners.github.io",  # run group website + route generator
]
OUT = Path("projects/vibe-coded.yml")
MAX_AGE_SECONDS = 60 * 60


def api(path):
    req = urllib.request.Request(
        f"https://api.github.com/{path}",
        headers={"Accept": "application/vnd.github+json"},
    )
    if os.environ.get("GITHUB_TOKEN"):
        req.add_header("Authorization", f"Bearer {os.environ['GITHUB_TOKEN']}")
    with urllib.request.urlopen(req, timeout=20) as resp:
        return json.load(resp)


def fetch():
    query = urllib.parse.urlencode(
        {"q": f"user:{USER} topic:{TOPIC} is:public", "sort": "updated", "per_page": 100}
    )
    items = api(f"search/repositories?{query}")["items"]

    for full_name in EXTRA_REPOS:
        try:
            items.append(api(f"repos/{full_name}"))
        except urllib.error.HTTPError as e:
            # a deleted or renamed-away repo shouldn't freeze the whole list;
            # anything else (rate limit, outage) falls through to main()
            if e.code != 404:
                raise
            print(f"fetch-vibe-coded: {full_name} not found; skipping", file=sys.stderr)

    seen = set()
    repos = []
    for r in items:
        # belt and braces: never publish a private repo, even if the token
        # used could see one; skip a pinned repo that's also topic-tagged
        if r["private"] or r["fork"] or r["archived"] or r["full_name"] in seen:
            continue
        seen.add(r["full_name"])
        repos.append(
            {
                "name": r["name"],
                "url": r["html_url"],
                "description": r["description"] or "",
                "homepage": r["homepage"] or "",
                "language": r["language"] or "",
                # the vibe-coded tag itself is implied by the page
                "topics": [t for t in r["topics"] if t != TOPIC],
                "stars": r["stargazers_count"],
                "updated": r["pushed_at"][:10],
            }
        )
    return repos


def main():
    fresh = OUT.exists() and time.time() - OUT.stat().st_mtime < MAX_AGE_SECONDS
    if fresh and not os.environ.get("CI"):
        return

    try:
        repos = fetch()
    except Exception as e:  # network, rate limit, bad JSON — never fail the build
        print(f"fetch-vibe-coded: {e}; keeping existing data", file=sys.stderr)
        if not OUT.exists():
            OUT.write_text("[]\n")
        return

    # JSON is valid YAML, and Quarto listings read .yml
    OUT.write_text(json.dumps(repos, indent=2) + "\n")
    print(f"fetch-vibe-coded: {len(repos)} repos -> {OUT}")


if __name__ == "__main__":
    main()
