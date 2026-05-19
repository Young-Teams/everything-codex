# EDA Journal Templates

LaTeX starting points for EDA/CAD journal submissions, currently covering:

| Template | Purpose | Primary Venue |
|----------|---------|---------------|
| [`tcad-regular/`](tcad-regular/) | Regular Paper (full IEEEtran journal layout) | IEEE TCAD, also usable for TVLSI |
| [`response-letter/`](response-letter/) | Point-by-point response to reviewers | All IEEE journals (TCAD/TVLSI/TODAES/ESL) |

## Which Template Do I Need?

| You are doing... | Template to use |
|------------------|-----------------|
| Drafting a new TCAD or TVLSI submission | `tcad-regular/` |
| Drafting a Brief / Short paper for TCAD | `tcad-regular/` (then trim to the brief page limit) |
| Drafting an IEEE ESL letter (4 pp.) | `tcad-regular/` (use `[journal]` doc class, then aggressively trim) |
| Drafting ACM TODAES submission | Use the ACM template from <https://www.acm.org/publications/proceedings-template> — not provided here yet |
| Replying to a Major / Minor Revision decision | `response-letter/` |
| Generating a diff PDF (revised vs prior) | Use `latexdiff`; see the `make diff` target in `tcad-regular/Makefile` |

## Prerequisites

All templates assume a working LaTeX installation (TeX Live or MiKTeX) with these packages:

- IEEEtran (download separately for `tcad-regular/`; see that template's README)
- amsmath, amsfonts, amssymb
- algorithm, algorithmic
- booktabs, multirow, array
- graphicx, subfig
- xcolor, hyperref, url
- tikz, pgfplots (pgfplots 1.18 or newer)
- listings
- cite (note: `cite`, not `natbib` — IEEEtran uses numeric citations)

For the response letter additionally: `enumitem`, `tcolorbox`, `geometry`.

On Ubuntu/Debian, the following typically covers everything:

```bash
sudo apt-get install texlive-full
```

On macOS with MacTeX, a `texlive-full` equivalent install also works.

## Quick Start: New TCAD Paper

```bash
# 1. Copy the template into your project
cp -r .agent/skills/eda-journal-writing/templates/tcad-regular my-tcad-paper
cd my-tcad-paper

# 2. Drop IEEEtran.cls and IEEEtran.bst here (download from CTAN)

# 3. Verify the template compiles as-is
make

# 4. Open main.pdf, then start replacing [REPLACE] markers
```

See [`tcad-regular/README.md`](tcad-regular/README.md) for full instructions.

## Quick Start: Revision Response Letter

```bash
# 1. Copy the response-letter template into your project
cp -r .agent/skills/eda-journal-writing/templates/response-letter my-paper-response

cd my-paper-response

# 2. Verify it compiles
make

# 3. Inventory reviewer comments, then fill in each [REPLACE] in response.tex
```

See [`response-letter/README.md`](response-letter/README.md) for full instructions, and [`../references/revision-workflow.md`](../references/revision-workflow.md) for the broader revision workflow.

## What These Templates Do *Not* Include

Intentionally omitted to keep the templates portable and small:

- **`IEEEtran.cls` / `IEEEtran.bst`** — Download separately from <https://www.ctan.org/pkg/ieeetran>. The IEEEtran package occasionally updates; using a current copy avoids version-drift issues.
- **Author photos for biographies** — Add to `figs/` only for the camera-ready phase, after acceptance.
- **A full `refs.bib`** — `tcad-regular/refs.bib` contains a small set of placeholder entries to show the expected fields. All real citations must be added through the citation workflow in [`../references/citation-workflow-ieee.md`](../references/citation-workflow-ieee.md).
- **An ACM TODAES template** — Use the official ACM template if you target TODAES. May be added here in a future version.

## Customization Tips

- **Macro naming**: `tcad-regular/main.tex` defines `\method{}` as a placeholder. Search-and-replace `\method` once you settle on the name.
- **Revision marking**: `\rev{}` (blue) and `\revtwo{}` (magenta) macros are pre-defined. Redefine them to no-ops in the camera-ready version.
- **Page budget**: For a 14-page TCAD target, aim for: Introduction ≤ 1.5 pages, Background+Related ≤ 2 pages, Method ≤ 4 pages, Experiments ≤ 4 pages, Discussion+Conclusion ≤ 1 page, References ≤ 1.5 pages.
- **Figures**: Use TikZ / PDF (vector), not raster. See `tcad-regular/content/03_method.tex` and `04_experiments.tex` for TikZ overview and pgfplots scaling examples.

## Related Reference Material

| Reference | Use When |
|-----------|----------|
| [`../references/writing-guide.md`](../references/writing-guide.md) | Narrative, abstract formula, Gopen & Swan, Perez tips, word choice, figure design |
| [`../references/tcad-submission-guide.md`](../references/tcad-submission-guide.md) | Pre-submission checklist, EDIcs categories, cover letter |
| [`../references/revision-workflow.md`](../references/revision-workflow.md) | When you receive a Major / Minor Revision decision |
| [`../references/citation-workflow-ieee.md`](../references/citation-workflow-ieee.md) | Verifying every citation programmatically |
| [`../references/sources.md`](../references/sources.md) | External links and bibliography |
