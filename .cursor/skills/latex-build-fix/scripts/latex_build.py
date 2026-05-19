#!/usr/bin/env python3
"""Run a fixed LaTeX build and clean auxiliary files by default."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path


PDFLATEX_ARGS = ["-interaction=nonstopmode", "-halt-on-error"]

AUX_EXTENSIONS = [
    ".aux",
    ".bbl",
    ".blg",
    ".log",
    ".out",
    ".toc",
    ".lof",
    ".lot",
    ".synctex.gz",
    ".fls",
    ".fdb_latexmk",
    ".bcf",
    ".run.xml",
    ".latex-build-fix.log",
]

DIAGNOSTIC_PATTERNS = [
    re.compile(r"^!"),
    re.compile(r"LaTeX Error:"),
    re.compile(r"Package .* Error:"),
    re.compile(r"Undefined control sequence"),
    re.compile(r"File `.*' not found"),
    re.compile(r"Emergency stop"),
    re.compile(r"Fatal error"),
    re.compile(r"Citation .* undefined"),
    re.compile(r"Reference .* undefined"),
    re.compile(r"There were undefined"),
    re.compile(r"Label\\(s\\) may have changed"),
    re.compile(r"Rerun to get"),
    re.compile(r"Warning--"),
    re.compile(r"Overfull \\\\hbox"),
    re.compile(r"Underfull \\\\hbox"),
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build LaTeX with pdflatex -> bibtex -> pdflatex -> pdflatex."
    )
    parser.add_argument(
        "entry",
        nargs="?",
        default="main.tex",
        help="LaTeX entry file, default: main.tex",
    )
    parser.add_argument(
        "--pdflatex",
        default="pdflatex",
        help="pdflatex executable name or path",
    )
    parser.add_argument(
        "--bibtex",
        default="bibtex",
        help="bibtex executable name or path",
    )
    parser.add_argument(
        "--clean-aux",
        action="store_true",
        help="clean generated auxiliary files after a successful build; this is the default",
    )
    parser.add_argument(
        "--keep-aux",
        action="store_true",
        help="keep generated auxiliary files after a successful build",
    )
    parser.add_argument(
        "--clean-only",
        action="store_true",
        help="only clean generated auxiliary files; do not build",
    )
    return parser.parse_args()


def run_stage(cmd: list[str], cwd: Path) -> tuple[int, str]:
    proc = subprocess.run(
        cmd,
        cwd=str(cwd),
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    return proc.returncode, proc.stdout


def collect_diagnostics(path: Path, limit: int) -> list[str]:
    if not path.exists():
        return []

    results: list[str] = []
    lines = path.read_text(errors="replace").splitlines()
    for idx, line in enumerate(lines, start=1):
        if any(pattern.search(line) for pattern in DIAGNOSTIC_PATTERNS):
            results.append(f"{path.name}:{idx}: {line}")
            if len(results) >= limit:
                break
    return results


def print_diagnostics(job_dir: Path, jobname: str, limit: int = 40) -> None:
    diagnostics = []
    diagnostics.extend(collect_diagnostics(job_dir / f"{jobname}.log", limit))
    diagnostics.extend(collect_diagnostics(job_dir / f"{jobname}.blg", limit))

    if diagnostics:
        print("\nDiagnostics:")
        for line in diagnostics[:limit]:
            print(f"  {line}")
    else:
        print("\nDiagnostics: no common LaTeX/BibTeX errors found in log files.")


def clean_aux_files(job_dir: Path, jobname: str) -> tuple[list[Path], list[str]]:
    removed: list[Path] = []
    errors: list[str] = []

    for extension in AUX_EXTENSIONS:
        path = job_dir / f"{jobname}{extension}"
        if not path.exists():
            continue
        if not path.is_file():
            errors.append(f"skip non-file auxiliary path: {path}")
            continue
        try:
            path.unlink()
            removed.append(path)
        except OSError as exc:
            errors.append(f"failed to remove {path}: {exc}")

    return removed, errors


def print_clean_summary(removed: list[Path], errors: list[str]) -> None:
    if removed:
        print("\nCleaned auxiliary files:")
        for path in removed:
            print(f"  {path}")
    else:
        print("\nCleaned auxiliary files: none found.")

    if errors:
        print("\nCleanup warnings:")
        for error in errors:
            print(f"  {error}")


def main() -> int:
    args = parse_args()
    entry = Path(args.entry).expanduser()
    if not entry.is_absolute():
        entry = Path.cwd() / entry
    entry = entry.resolve()

    if not entry.exists():
        print(f"error: entry file not found: {entry}", file=sys.stderr)
        return 2
    if entry.suffix.lower() != ".tex":
        print(f"error: entry file must be a .tex file: {entry}", file=sys.stderr)
        return 2

    job_dir = entry.parent
    tex_name = entry.name
    jobname = entry.stem
    transcript_path = job_dir / f"{jobname}.latex-build-fix.log"

    if args.clean_only:
        removed, errors = clean_aux_files(job_dir, jobname)
        print_clean_summary(removed, errors)
        return 1 if errors else 0

    stages = [
        ("pdflatex #1", [args.pdflatex, *PDFLATEX_ARGS, tex_name]),
        ("bibtex", [args.bibtex, jobname]),
        ("pdflatex #2", [args.pdflatex, *PDFLATEX_ARGS, tex_name]),
        ("pdflatex #3", [args.pdflatex, *PDFLATEX_ARGS, tex_name]),
    ]

    transcript_parts: list[str] = []
    failed = False

    for label, cmd in stages:
        print(f"==> {label}: {' '.join(cmd)}")
        returncode, output = run_stage(cmd, job_dir)
        transcript_parts.append(f"$ {' '.join(cmd)}\n{output}\n")
        print(f"    exit code: {returncode}")
        if returncode != 0:
            failed = True
            break

    transcript_path.write_text("\n".join(transcript_parts), encoding="utf-8")
    print(f"\nTranscript: {transcript_path}")
    print_diagnostics(job_dir, jobname)

    pdf_path = job_dir / f"{jobname}.pdf"
    if failed:
        print("\nBuild failed.")
        return 1
    if not pdf_path.exists():
        print(f"\nBuild finished but PDF was not found: {pdf_path}")
        return 1

    print(f"\nBuild succeeded: {pdf_path}")
    if not args.keep_aux:
        removed, errors = clean_aux_files(job_dir, jobname)
        print_clean_summary(removed, errors)
        if errors:
            return 1
    else:
        print("\nAuxiliary files kept because --keep-aux was set.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
