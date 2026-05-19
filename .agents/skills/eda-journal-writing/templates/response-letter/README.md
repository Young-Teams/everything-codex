# Response-to-Reviewers Letter Template

A standalone LaTeX document for the **point-by-point response** required by every IEEE TCAD / TVLSI / TODAES / ESL revision. The compiled `response.pdf` is submitted via ScholarOne alongside the revised manuscript.

## Files

```
response-letter/
├── response.tex       # The point-by-point response document
├── Makefile           # `make` to build, `make clean` / `make distclean`
└── README.md          # This file
```

## What This Template Provides

- **Custom environments** for cleanly quoting reviewer comments and your responses:
  - `\begin{reviewercomment}{R1.C1} ... \end{reviewercomment}` — boxed gray quote
  - `\response` — opens the response with a colored "Response:" prefix
  - `\paperref{Sec. III-B, p. 6, lines 12--19}` — cross-reference to the revised paper
  - `\begin{revexcerpt} ... \end{revexcerpt}` — quote new text from the revised manuscript

- **Sectioned structure** following IEEE TCAD conventions:
  1. Opening paragraph + summary of main changes
  2. Response to the Editor
  3. Response to Reviewer 1 (with examples of agreement and disagreement)
  4. Response to Reviewer 2
  5. Response to Reviewer 3
  6. Summary of Changes
  7. New citations introduced + diff PDF note

- **Examples of the 4-part response pattern** (Quote → Acknowledge → Action → Result) for:
  - Agreement-and-fix
  - Correction the reviewer caught
  - Respectful disagreement (with manuscript-level clarification)

## How To Use

### 1. Compile the empty template

```bash
make
```

You should get a clean `response.pdf` showing the placeholder content.

### 2. Inventory every reviewer comment

Before writing anything, extract every comment from the decision letter into a flat numbered list:

```
R1.C1: ...
R1.C2: ...
R2.C1: ...
R3.C1: ...
```

This list is what you will respond to one by one.

### 3. Categorize each comment

For each comment, decide:

- **Agree-and-fix** — make the change, write a short response describing what changed.
- **Partial-agree-and-clarify** — make a partial change, add a paper-level clarification.
- **Respectfully-disagree** — explain your reasoning AND still add a clarification to the paper.

See `../../references/revision-workflow.md` for the full guidance and rules.

### 4. Edit `response.tex`

Replace every `[REPLACE]` marker with:

- Quote the reviewer's comment verbatim inside `\begin{reviewercomment}{R1.C1}...\end{reviewercomment}`.
- Write your response below `\response`, structured as:
  - Acknowledge in one short sentence (no sycophancy).
  - Describe the action you took, with a `\paperref{}` to the specific section / page / line in the revised manuscript.
  - State the resulting outcome (the concrete improvement / clarification).
  - Optionally include `\begin{revexcerpt}...\end{revexcerpt}` quoting the new text.

### 5. Cross-check against the revised manuscript

After both `response.pdf` and the revised `main.pdf` are ready, do a final cross-check:

- [ ] Every action mentioned in `response.pdf` actually exists in `main.pdf`.
- [ ] Section / page / line references in `\paperref{...}` are accurate.
- [ ] Every new citation mentioned in the response also appears in `refs.bib` of the manuscript.
- [ ] The "Main changes" bullets in the opening match the "Summary of Changes" at the end.

### 6. Submit

Submit all three:

1. Revised manuscript PDF (`main.pdf`)
2. This response letter PDF (`response.pdf`)
3. Optional but strongly recommended: `latexdiff`-generated diff PDF (`main-diff.pdf`)

via ScholarOne.

## Key Rules (from `../../references/revision-workflow.md`)

1. **Quote each reviewer comment verbatim** before responding.
2. **Thank the reviewer** for each substantive comment (one sentence, not sycophantic).
3. **Always cite specific manuscript locations** ("see Sec. III-B, lines 12--19 of page 6").
4. **Never refuse a comment without also adding a clarification to the paper.**
5. **Use color in the manuscript** (or `latexdiff`) to mark all changes — make life easy for the reviewer.
6. **Re-verify any new citations** programmatically (see `../../references/citation-workflow-ieee.md`).
7. **Re-run all old experiments** if you changed anything that might affect them.
8. **Sanity-check that the response letter and the revised manuscript do not contradict each other.**
