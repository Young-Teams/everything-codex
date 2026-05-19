# TCAD Regular Paper Template

A complete IEEEtran-based starting point for an IEEE TCAD Regular Paper submission. Drop your `IEEEtran.cls` and `IEEEtran.bst` next to `main.tex`, then `make`.

## Files

```
tcad-regular/
├── main.tex              # Top-level document (title, authors, includes)
├── refs.bib              # Bibliography starter with placeholder entries
├── Makefile              # `make` to build; `make diff` for revision diff
├── README.md             # This file
├── content/
│   ├── 01_intro.tex
│   ├── 02_background.tex
│   ├── 03_method.tex
│   ├── 04_experiments.tex
│   ├── 05_discussion.tex
│   └── 06_conclusion.tex
└── figs/                 # Your figures go here (empty placeholder dir)
```

## Setup

### 1. Place `IEEEtran.cls` and `IEEEtran.bst`

This template intentionally does NOT ship `IEEEtran.cls`. Get a current copy from one of:

- CTAN: <https://www.ctan.org/pkg/ieeetran>
- IEEE Author Tools: <https://www.ieee.org/conferences/publishing/templates.html>
- An existing copy you already have (e.g., from a previous IEEE paper)

After downloading, you should have at minimum:

```
IEEEtran.cls
IEEEtran.bst
```

Place both in the same directory as `main.tex`.

### 2. Verify the template compiles

Before you write anything:

```bash
make
```

You should get a clean `main.pdf` showing the placeholder content. If this fails, fix the build environment before editing content.

Common issues:

- **Missing IEEEtran.cls** — see step 1.
- **Missing `algorithm` / `algorithmic`** packages — `tlmgr install algorithms` (TeX Live) or install via your distribution.
- **Missing `pgfplots`** — `tlmgr install pgfplots`.
- **`Undefined control sequence \IEEEPARstart`** — your `IEEEtran.cls` may be very old; download a more recent one.

### 3. Replace placeholder content

Work through, in order:

1. `main.tex`: title, authors, abstract, keywords, `\markboth{}`
2. `content/01_intro.tex`: contribution bullets, problem context
3. `content/02_background.tex`: background + related work
4. `content/03_method.tex`: method + algorithm + complexity
5. `content/04_experiments.tex`: setup + main + ablation + scaling
6. `content/05_discussion.tex`: limitations + future work
7. `content/06_conclusion.tex`: short conclusion
8. `refs.bib`: replace EVERY `PLACEHOLDER_*` entry with verified BibTeX
   (see `../../references/citation-workflow-ieee.md`)

After each section, compile (`make` or `make quick`) to catch errors early.

## Useful Macros (already in `main.tex`)

| Macro | Purpose |
|-------|---------|
| `\method{}` | Your method's name, used consistently throughout |
| `\eg{} \ie{} \etal{}` | Properly-spaced abbreviations |
| `\WNS \TNS \HPWL \QoR` | Common EDA acronyms |
| `\rev{...}` | Mark first-round revisions (blue text) |
| `\revtwo{...}` | Mark second-round revisions (magenta text) |

For camera-ready, redefine the revision macros to no-ops:

```latex
\renewcommand{\rev}[1]{#1}
\renewcommand{\revtwo}[1]{#1}
```

## Building

```bash
make             # Full build (with bibtex). Uses latexmk if available.
make quick       # Single pdflatex pass (fast iteration; no refs).
make diff        # latexdiff against a previous-round main-prev.tex
make clean       # Remove .aux/.log/etc. (keep PDF).
make distclean   # Remove everything generated.
```

## Submission Checklist

Before submitting via ScholarOne:

- [ ] `make distclean && make` produces a clean `main.pdf`
- [ ] Page count is ≤ 14 (or you accept overlength fees)
- [ ] No remaining `PLACEHOLDER_*` references
- [ ] All citations are verified (see `../../references/citation-workflow-ieee.md`)
- [ ] `\rev{}` and `\revtwo{}` are either removed or redefined to no-ops (final version only)
- [ ] Author block matches the blind/non-blind policy of your submission round
- [ ] `\markboth{}` is updated with your final title
- [ ] All `[REPLACE]` markers are addressed
- [ ] Figures are vector (PDF/EPS/TikZ), not raster
- [ ] Tables use `booktabs`, captions above
- [ ] Figures have captions below

For the complete submission checklist, see `../../references/tcad-submission-guide.md`.

## Diff PDF for Revisions

When you receive a Major / Minor Revision decision and need to submit a revised manuscript:

1. Copy your previously-submitted `main.tex` to `main-prev.tex`.
2. Edit `main.tex` and `content/*.tex` as needed, using `\rev{...}` for changes.
3. Run `make diff` to produce `main-diff.pdf`.
4. Submit `main.pdf` (the new manuscript) AND `main-diff.pdf` (as supplementary) AND your response letter (use the `response-letter` template).

See `../../references/revision-workflow.md` for full guidance.
