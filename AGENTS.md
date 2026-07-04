# Project: chendaniely.github.io

Personal website and blog for Daniel Chen.
Built with **Quarto** as a static site,
deployed via GitHub Pages on the `gh-pages` branch.

## Writing conventions

When creating commits, preface each commit with a `🤖: ` so it's easy to see a claude commit.

### Semantic line breaks

All prose in this repository (`.md`, `.qmd`, `AGENTS.md`, `CLAUDE.md`) uses semantic line breaks (SEMBR):
break lines at natural sentence and clause boundaries,
not at a fixed character width.
Each sentence or major clause goes on its own line.
This keeps diffs readable — one idea changed = one line changed.

Do not reflow prose into long single lines or hard-wrap at 80 characters.

## Repository layout

```
_quarto.yml          # Quarto site config (cosmo + brand + theme.scss)
_variables.yml       # "now" values, injected with {{< var now.* >}}
theme.scss           # ALL custom styling (commented, sectioned)
theme-dark.scss      # dark-mode color overrides
scroll-reveal.html   # the site's only JS (~20 lines)
_now-signposts.qmd   # home page signpost cards partial
talks/ teaching/ projects/   # section stub pages
posts/               # All blog posts — one folder per post
  YYYY/
    YYYY-MM-DD-slug/
      index.md       # Plain markdown (older migrated posts)
      index.qmd      # Quarto post (newer or converted from Rmd)
      *.jpg/png      # Images co-located with their post
posts/2026/          # Active/new posts
_content_old/        # Reference only — old Hugo Apero source (md/Rmd)
                     # Ignored by Quarto (underscore prefix). Do not edit.
submodules/          # Git submodules (e.g. yvr-cherry-blossoms data)
_site/               # Build output — never edit directly, in .gitignore
Makefile             # `make submodules` to init/update submodules
```

## Branches

| Branch | Purpose |
|--------|---------|
| `main` | Source — edit here |
| `gh-pages` | Deployed site output — do not edit manually |
| `master` | Old Hugo/blogdown rendered site — reference only |

## Blog post conventions

- Every post lives in its own folder: `posts/YYYY/YYYY-MM-DD-slug/index.md` (or `.qmd`)
- Images and assets are co-located in the same folder as `index.*`
- New posts should use `.qmd`;
  migrated posts may stay as `.md` until converted
- Quarto categories are used for both categories and tags
  (no separate tags concept)
- Old posts have Hugo/Jekyll frontmatter (`layout:`, `permalink:`, `slug:`, etc.) —
  leave it in place until the post is fully converted to Quarto

## Interactive posts

Posts can embed interactive charts with Quarto's built-in `ojs` engine —
no site-level JavaScript needed.
See `posts/2026/2026-07-04-interactive-posts/` for the pattern.

## Updating "what's current"

Edit `_variables.yml` (next talk, current courses, current project).
Values surface on the home page signposts and the Talks page banner
via `{{< var now.* >}}`.
Blank a value with `""`; don't delete keys.

## Planned work

See `_TODO.md` in the repo root for full context on planned projects.

## Open work (GitHub issues)

- **Issue #30**: Add `aliases:` to all posts for old-format URL redirects
  Old URL pattern: `/YYYY/MM/DD/slug/`
  New URL pattern: `/posts/YYYY/YYYY-MM-DD-slug/`
  Three frontmatter cases:
  posts with `permalink:`,
  posts with `slug:`,
  posts with neither (derive from folder name).

- **Issue #29**: Create stub posts for external blog contributions
  - 7 new stubs needed for Carpentries posts (2015–2022) not already in `posts/`
  - 7 existing posts need the Carpentries URL added to frontmatter
  - 3 Posit/RStudio open source blog posts need stubs

## Post migration history

Posts were migrated from: WordPress → Jekyll → Hugo/blogdown → Quarto.
The `_content_old/blog/` directory contains the Hugo Apero `.md`/`.Rmd` source
used as reference.
Posts were moved into `posts/` via `git mv` to preserve commit history —
use `git log --follow` to trace a file back through renames.

## Building and previewing

```bash
quarto preview    # live preview at localhost
quarto render     # full build to _site/
make submodules   # init/update git submodules
```

## Deployment

Pushing to `main` triggers GitHub Actions
which renders the site and pushes output to `gh-pages`.
Do not push directly to `gh-pages`.
