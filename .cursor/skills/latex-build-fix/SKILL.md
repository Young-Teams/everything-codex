---
name: latex-build-fix
description: Build and repair LaTeX projects using the fixed sequence pdflatex, bibtex, pdflatex, pdflatex. Use when Codex needs to compile a LaTeX entry file such as main.tex, inspect .log/.blg output, diagnose missing packages, undefined commands, citation/reference problems, BibTeX issues, or make targeted source fixes until the PDF builds.
---

# LaTeX Build Fix

## Overview

Use this skill to compile LaTeX papers with a deterministic IEEE-style build chain and to repair build failures from the generated logs. Prefer the bundled script for repeatable builds, then inspect source files and apply minimal fixes. The bundled script cleans auxiliary files after a successful build by default.

## Build Workflow

1. Identify the entry file. Default to `main.tex` in the current workspace unless the user names another `.tex` file.
2. Run the bundled script from the project root:

```bash
python3 .codex/skills/latex-build-fix/scripts/latex_build.py main.tex
```

3. If the script fails, inspect the first fatal error in its summary, then read the relevant `.log`, `.blg`, `.aux`, and source file lines.
4. Fix the smallest source issue that explains the failure. Do not rewrite unrelated paper content.
5. Re-run the same script until it exits successfully or a genuine external dependency is missing.

## What Counts as Fixed

Treat the build as fixed when the script exits with code 0 and the final `main.pdf` or matching job-name PDF exists. Warnings such as overfull/underfull boxes and incomplete bibliography metadata do not block PDF generation, but mention them if they remain.

Clean generated auxiliary files by default after a successful build. If the user explicitly asks to keep auxiliary files or logs, pass `--keep-aux`. Cleanup removes only generated LaTeX artifacts for the job name (`.aux`, `.bbl`, `.blg`, `.log`, `.out`, `.toc`, `.lof`, `.lot`, `.synctex.gz`, `.fls`, `.fdb_latexmk`, `.bcf`, `.run.xml`, `.latex-build-fix.log`). Do not delete source `.tex`, `.bib`, figures, class files, or the final PDF unless explicitly requested.

## Repair Heuristics

- For `Undefined control sequence`, inspect the command and add the established package or replace the command with the local convention.
- For `File ... not found`, check spelling and project-relative paths before adding packages.
- For citation problems, verify `\bibliography{...}` paths and `.bib` keys; run the full chain again after edits.
- For reference problems, confirm labels exist and run the full chain twice after edits.
- For IEEEtran papers, prefer `cite`, `subfig` with `caption=false`, and `IEEEtran` bibliography style unless the project already has a different explicit target.

## Script

`scripts/latex_build.py` runs:

```text
pdflatex -interaction=nonstopmode -halt-on-error <entry.tex>
bibtex <jobname>
pdflatex -interaction=nonstopmode -halt-on-error <entry.tex>
pdflatex -interaction=nonstopmode -halt-on-error <entry.tex>
```

It prints each stage, stores a combined transcript in `<jobname>.latex-build-fix.log`, summarizes likely actionable diagnostics from `<jobname>.log` and `<jobname>.blg`, and then cleans generated auxiliary files after a successful build.

When the user explicitly asks to keep auxiliary files or logs, use:

```bash
python3 .codex/skills/latex-build-fix/scripts/latex_build.py main.tex --keep-aux
```

When the user asks only to remove generated auxiliary files without rebuilding, use:

```bash
python3 .codex/skills/latex-build-fix/scripts/latex_build.py main.tex --clean-only
```

The legacy `--clean-aux` flag is accepted but unnecessary because cleanup is now the default after a successful build.
