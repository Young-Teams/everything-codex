---
name: eda-journal-writing
description: Write publication-ready EDA/CAD journal papers for IEEE TCAD, IEEE TVLSI, ACM TODAES, and IEEE ESL. Use when drafting EDA/CAD/hardware journal papers from a research repo, structuring arguments for an IEEE Transactions audience, formatting with IEEEtran, preparing major/minor revisions, or writing response-to-reviewers letters.
version: 1.1.0
author: RTLCraft
license: MIT
tags: [Academic Writing, TCAD, TVLSI, TODAES, IEEE Transactions, EDA, CAD, LaTeX, IEEEtran, Paper Writing, Citations, Research, Hardware]
dependencies: [semanticscholar, requests]
---

# EDA Journal Writing for IEEE TCAD and Related Venues

Expert-level guidance for writing publication-ready papers targeting EDA/CAD journals: **IEEE TCAD, IEEE TVLSI, ACM TODAES, IEEE ESL**, and adjacent venues. This skill combines general scientific writing philosophy from leading researchers (Nanda, Farquhar, Gopen & Swan, Lipton, Perez, Steinhardt) with practical tools: an IEEEtran LaTeX template, a citation verification workflow tuned to IEEE Xplore / DBLP, a response-to-reviewers letter template, and a TCAD submission checklist.

## Core Philosophy: Collaborative Writing

**Paper writing is collaborative, but Claude should be proactive in delivering drafts.**

The typical workflow starts with a research repository containing code, results, and experimental artifacts. Claude's role is to:

1. **Understand the project** by exploring the repo, results, and existing documentation
2. **Deliver a complete first draft** when confident about the contribution
3. **Search literature** using web search and APIs to find relevant citations
4. **Refine through feedback cycles** when the scientist provides input
5. **Ask for clarification** only when genuinely uncertain about key decisions

**Key Principle**: Be proactive. If the repo and results are clear, deliver a full draft. Don't block waiting for feedback on every section—scientists are busy. Produce something concrete they can react to, then iterate based on their response.

---

## ⚠️ CRITICAL: Never Hallucinate Citations

**This is the most important rule in academic writing with AI assistance.**

### The Problem

AI-generated citations have a **~40% error rate**. Hallucinated references—papers that don't exist, wrong authors, incorrect years, fabricated DOIs—are a serious form of academic misconduct that can result in desk rejection or retraction. TCAD/TVLSI editors are experienced and routinely catch fabricated citations.

### The Rule

**NEVER generate BibTeX entries from memory. ALWAYS fetch programmatically.**

| Action | ✅ Correct | ❌ Wrong |
|--------|-----------|----------|
| Adding a citation | Search IEEE Xplore / DBLP / CrossRef → verify → fetch BibTeX | Write BibTeX from memory |
| Uncertain about a paper | Mark as `[CITATION NEEDED]` | Guess the reference |
| Can't find exact paper | Note: "placeholder - verify" | Invent similar-sounding paper |
| IEEE Xplore paper | Use Xplore's "Cite This → BibTeX" button | Reconstruct from title |

### When You Can't Verify a Citation

If you cannot programmatically verify a citation, you MUST:

```latex
% EXPLICIT PLACEHOLDER - requires human verification
\cite{PLACEHOLDER_author2024_verify_this}  % TODO: Verify this citation exists
```

**Always tell the scientist**: "I've marked [X] citations as placeholders that need verification. I could not confirm these papers exist."

See [references/citation-workflow-ieee.md](references/citation-workflow-ieee.md) for the full IEEE-style verification workflow (IEEE Xplore + DBLP + CrossRef + Semantic Scholar).

---

## Workflow 0: Starting from a Research Repository

When beginning paper writing, start by understanding the project:

```
Project Understanding:
- [ ] Step 1: Explore the repository structure
- [ ] Step 2: Read README, existing docs, and key results
- [ ] Step 3: Identify the main contribution with the scientist
- [ ] Step 4: Find papers already cited in the codebase
- [ ] Step 5: Search for additional relevant literature
- [ ] Step 6: Outline the paper structure together
- [ ] Step 7: Draft sections iteratively with feedback
```

**Step 1: Explore the Repository**

```bash
# Understand project structure
ls -la
find . -name "*.py" -o -name "*.v" -o -name "*.sv" -o -name "*.scala" | head -30
find . -name "*.md" -o -name "*.txt" | xargs grep -l -i "result\|conclusion\|finding" 2>/dev/null
```

Look for:
- `README.md` — Project overview and claims
- `results/`, `outputs/`, `experiments/`, `logs/` — Key findings
- `configs/`, `scripts/` — Experimental settings the paper must document
- Existing `.bib` files or citation references
- Any draft documents, design notes, or RFCs

**Step 2: Identify Existing Citations in the Repo**

```bash
# Find existing citations
grep -rE "arxiv|doi|cite|@(article|inproceedings)" \
     --include="*.md" --include="*.bib" --include="*.py" --include="*.tex"
find . -name "*.bib"
```

These are high-signal starting points for Related Work — the scientist has already deemed them relevant.

**Step 3: Clarify the Contribution**

Before writing, explicitly confirm with the scientist:

> "Based on my understanding of the repo, the main contribution appears to be [X].
> The key results show [Y]. Is this the framing you want for the paper,
> or should we emphasize different aspects?"

**Never assume the narrative — always verify with the human.**

**Step 4: Search for Additional Literature**

Use web search + the right academic sources to find relevant papers. For EDA papers, the priority order is:

1. **IEEE Xplore** — for any IEEE conference/journal paper (DAC, ICCAD, DATE, TCAD, TVLSI, ASP-DAC, ISLPED)
2. **ACM Digital Library** — for ACM venues (ISPD, GLSVLSI, FPGA, some DAC years)
3. **DBLP** — fastest unified search by author or topic
4. **Semantic Scholar / arXiv** — for cross-source coverage and preprints

```
Search queries to try:
- "[main technique] + [application domain]"
- "[baseline method] comparison"
- "[problem name] state-of-the-art"
- Author names from existing citations
```

Then verify and retrieve BibTeX using the citation workflow ([references/citation-workflow-ieee.md](references/citation-workflow-ieee.md)).

**Step 5: Deliver a First Draft**

**Be proactive — deliver a complete draft rather than asking permission for each section.**

If the repo provides clear results and the contribution is apparent:

1. Write the full first draft end-to-end into the TCAD template
2. Present the complete draft for feedback
3. Iterate based on scientist's response

If genuinely uncertain about framing or major claims:

1. Draft what you can confidently
2. Flag specific uncertainties: "I framed X as the main contribution—let me know if you'd prefer to emphasize Y instead"
3. Continue with the draft rather than blocking

---

## When to Use This Skill

Use this skill when:

- **Starting from a research repo** to write an EDA/CAD journal paper
- **Drafting or revising** specific sections
- **Finding and verifying citations** for related work
- **Formatting** with IEEEtran for journal submission
- **Converting** a conference paper (e.g., DAC, ICCAD, DATE, ASP-DAC) to journal form
- **Preparing major/minor revision** and the response-to-reviewers letter
- **Iterating** on drafts with scientist feedback

**Always remember**: First drafts are starting points for discussion, not final outputs.

---

## Balancing Proactivity and Collaboration

**Default: Be proactive. Deliver drafts, then iterate.**

| Confidence Level | Action |
|------------------|--------|
| **High** (clear repo, obvious contribution) | Write full draft, deliver, iterate on feedback |
| **Medium** (some ambiguity) | Write draft with flagged uncertainties, continue |
| **Low** (major unknowns) | Ask 1-2 targeted questions, then draft |

**Draft first, ask with the draft** (not before):

| Section | Draft Autonomously | Flag With Draft |
|---------|-------------------|-----------------|
| Abstract | Yes | "Framed contribution as X—adjust if needed" |
| Introduction | Yes | "Emphasized problem Y—correct if wrong" |
| Methods | Yes | "Included details A, B, C—add missing pieces" |
| Experiments | Yes | "Highlighted results 1, 2, 3—reorder if needed" |
| Background & Related Work | Yes | "Cited papers X, Y, Z—add any I missed" |

**Only block for input when:**

- The target venue is unclear (TCAD vs TVLSI vs a conference — affects page limits, scope)
- The paper is a **revision** — you need the editor's decision letter and reviewer comments first
- Multiple contradictory framings seem equally valid
- Results appear incomplete or inconsistent

**Don't block for:**

- Word choice decisions
- Section ordering
- Which specific results to highlight (make a choice, flag it)
- Citation completeness (draft with what you find, note gaps)

---

## The Narrative Principle

**The single most critical insight**: your paper is not a collection of experiments — it's a story with one clear contribution supported by evidence.

> "A paper is a short, rigorous, evidence-based technical story with a takeaway readers care about." — Neel Nanda

**Three Pillars** (must be crystal clear by the end of introduction):

| Pillar | Description | Example |
|--------|-------------|---------|
| **The What** | 1-3 specific novel claims within a cohesive theme | "We prove that X achieves Y under condition Z" |
| **The Why** | Rigorous empirical evidence supporting the claims | Strong baselines honestly tuned, experiments distinguishing hypotheses |
| **The So What** | Why readers should care | Connection to recognized community problems |

**If you cannot state your contribution in one sentence, you don't yet have a paper.**

---

## Paper Structure Workflow

### Workflow 1: Writing a Complete Paper (Iterative)

Copy this checklist and track progress. **Each step involves drafting → feedback → revision:**

```
Paper Writing Progress:
- [ ] Step 1: Define the one-sentence contribution (with scientist)
- [ ] Step 2: Draft Figure 1 → get feedback → revise
- [ ] Step 3: Draft abstract → get feedback → revise
- [ ] Step 4: Draft introduction → get feedback → revise
- [ ] Step 5: Draft methods → get feedback → revise
- [ ] Step 6: Draft experiments → get feedback → revise
- [ ] Step 7: Draft Background & Related Work (one combined section) → get feedback → revise
- [ ] Step 8: Draft discussion / limitations → get feedback → revise
- [ ] Step 9: Verify all citations programmatically
- [ ] Step 10: Run the submission checklist (references/tcad-submission-guide.md)
- [ ] Step 11: Final review cycle and submission
```

> **Paper Section Layout (TCAD / TVLSI convention).** The body of an EDA/CAD journal paper is organized as a fixed sequence of top-level sections: **Introduction → Background and Related Work → Proposed Method → Experiments → Discussion / Limitations → Conclusion.** Background material (terminology, formal definitions, primers on prior techniques) and the survey of prior work are written **together in a single Section II** — typically titled "Background and Related Work" (or just "Background", or just "Related Work" — pick one). Do **not** carve this section into "Background" vs. "Related Work" subsections, and do **not** promote them to two peer top-level sections. If you need subsections at all, group them **by topic / approach** (e.g., `II.A Python-Embedded HDLs`, `II.B LLM-Driven RTL Generation`, `II.C Verification Frameworks`), not by the "background vs. related work" distinction. The Step 7 draft order above is the recommended *writing* order, not the in-paper order.

**Step 1: Define the One-Sentence Contribution**

**This step requires explicit confirmation from the scientist.**

Before writing anything, articulate and verify:
- What is the single thing your paper contributes?
- What was not obvious or present before your work?

> "I propose framing the contribution as: '[one sentence]'. Does this capture
> what you see as the main takeaway? Should we adjust the emphasis?"

**Step 2: Draft Figure 1**

Figure 1 deserves special attention — many readers skip directly to it.

- Convey the core idea, approach, or most compelling result
- Use vector graphics (TikZ/PDF/EPS for plots); avoid raster in two-column IEEEtran
- Write captions that stand alone without main text
- Ensure readability in black-and-white (8% of men have color vision deficiency)

**Step 3: Write Abstract (5-Sentence Formula)**

From Sebastian Farquhar (DeepMind):

```
1. What you achieved: "We introduce...", "We propose...", "We demonstrate..."
2. Why this is hard and important
3. How you do it (with specialist keywords for discoverability)
4. What evidence you have
5. Your most remarkable number/result
```

**Delete** generic openings ("Large language models have achieved remarkable success...", "The continued scaling of integrated circuits..."). Start with your specific contribution.

**Step 4: Write Introduction**

Must include:

- Clear problem statement
- Brief positioning of prior approaches
- 2-4 bullet contribution list (each 1-3 lines in two-column format)
- Brief preview of headline results

Length target for a 14-page TCAD Regular Paper: introduction 1.5–2 pages; Method/Approach should start by **page 3–4** (not page 2 as in 8–9 page ML conferences). See the full Length Budget table in [references/writing-guide.md](references/writing-guide.md#length-budget-for-ieee-transactions-papers).

**Step 5: Methods Section**

Enable reimplementation:

- Conceptual outline or pseudocode (use `algorithm` + `algorithmic`)
- All hyperparameters and design decisions listed
- Architectural / algorithmic details sufficient for reproduction
- Present the final design; ablations go in experiments

**Step 6: Experiments Section**

For each experiment, explicitly state:

- What claim it supports
- How it connects to the main contribution
- Experimental setting (with details that aid reproducibility — tools, configurations, datasets/benchmarks the project actually uses)
- What to observe: "the blue line shows X, which demonstrates Y"

Choose what's reproducibility-relevant to your project — the domain scientist is the source of truth for which tools, benchmarks, metrics, and configurations are standard in their sub-area.

**Step 7: Background and Related Work (single combined section, no `Background`/`Related Work` subsection split)**

This is **one** top-level section of the paper — typically **Section II**, titled "Background and Related Work" (or simply "Background", or simply "Related Work" — pick one name). The combined section absorbs both the technical primer (terminology, formal definitions, prior techniques the reader must know) and the survey of prior work; they live in the same prose, not in two clearly labeled halves.

**Do not split by type.** The following are all wrong:

- ❌ Two peer top-level sections — `\section{Background}` followed by `\section{Related Work}`
- ❌ Two subsections inside Section II named `\subsection{Background}` and `\subsection{Related Work}`
- ❌ A "Preliminaries" section *and* a "Related Work" section as siblings

**Use subsections only when grouping by topic / approach.** A typical structure for an EDA journal paper is:

```
II. Background and Related Work
    II.A  [Topic / approach group 1]   (e.g., Python-embedded HDLs)
    II.B  [Topic / approach group 2]   (e.g., LLM-driven RTL generation and EDA agents)
    II.C  [Topic / approach group 3]   (e.g., Python verification frameworks)
    II.D  [Topic / approach group 4]   (e.g., the gap our method closes)
```

A short paper, or one whose field needs no primer, can also be a flat section with no subsections at all. Both are fine; what is **not** fine is naming the subsections "Background" and "Related Work".

For the content itself, organize **methodologically, not paper-by-paper**:

**Good:** "One line of work uses Floogledoodle's assumption [refs] whereas we use Doobersnoddle's assumption because..."

**Bad:** "Snap et al. introduced X while Crackle et al. introduced Y."

Cite generously — reviewers likely authored relevant papers.

**Step 8: Discussion / Limitations**

TCAD does not require a "Limitations" section, but honest discussion of scope, threats to validity, and design choices is appreciated by reviewers. Pre-empting criticisms is far better than letting reviewers raise them.

**Step 9: Verify Citations**

See [references/citation-workflow-ieee.md](references/citation-workflow-ieee.md).

**Steps 10–11: Submission Checks**

See [references/tcad-submission-guide.md](references/tcad-submission-guide.md).

---

## Writing Philosophy

**See [references/writing-guide.md](references/writing-guide.md) for the full reference covering:**

- The Narrative Principle (Nanda) and one-contribution focus (Karpathy)
- Time allocation across abstract / intro / figures / rest (Nanda)
- 5-sentence abstract formula (Farquhar)
- Introduction structure with contribution bullets
- Gopen & Swan's 7 principles of reader expectations
- Ethan Perez micro-tips (pronoun management, verb placement, filler words)
- Zachary Lipton on word choice (eliminate hedging, vacuous intensifiers)
- Jacob Steinhardt on precision and consistent terminology
- Mathematical writing conventions
- Figure design (colorblind-safe palettes, captions, vector graphics)
- Common mistakes and a pre-submission checklist

### Time Allocation (From Nanda)

Spend approximately **equal time** on each of:

1. The abstract
2. The introduction
3. The figures
4. Everything else combined

**Why?** Most reviewers form judgments before reaching your methods. Readers encounter your paper as: **title → abstract → introduction → figures → maybe the rest.**

### What Reviewers Actually Read

| Paper Section | % Reviewers Who Read | Implication |
|---------------|---------------------|-------------|
| Abstract | 100% | Must be perfect |
| Introduction | 90%+ (skimmed) | Front-load contribution |
| Figures | Examined before methods | Figure 1 is critical |
| Methods | Only if interested | Don't bury the lede |
| Appendix | Rarely | Put only supplementary details |

**Bottom line**: if your abstract and intro don't hook reviewers, they may never read your brilliant methods section.

---

## Venue Requirements Quick Reference

| Venue | Page Limit (Regular) | Layout | Blind Review | Revisions Typical |
|-------|----------------------|--------|--------------|-------------------|
| **IEEE TCAD** | ~14 pages (overlength charged) | 2-col, 10pt, IEEEtran | Single-blind (verify per-year) | 2-3 rounds |
| **IEEE TVLSI** | ~10-12 pages | 2-col, 10pt, IEEEtran | Single-blind | 2-3 rounds |
| **ACM TODAES** | ~25 pages | ACM journal style | Single-blind | 2-3 rounds |
| **IEEE ESL** | 4 pages (letters) | 2-col, 10pt, IEEEtran | Single-blind | 1-2 rounds |

**Universal requirements for IEEE journals covered by this skill:**

- IEEEtran with `[journal,letterpaper]` document class options
- Numeric `\cite{...}` (from the `cite` package), not author-year
- References don't count toward page budget but pile up at the end (~1-2 pages typical)
- IEEEtran requires figures **with caption below**, tables **with caption above**

See [references/tcad-submission-guide.md](references/tcad-submission-guide.md) for TCAD-specific facts (EDIcs categories, cover letter format, ScholarOne tips, camera-ready biographies).

---

## Using the LaTeX Template

### Workflow 4: Starting a New Paper from Template

**Always copy the entire template directory first, then write within it.**

```
Template Setup Checklist:
- [ ] Step 1: Copy templates/tcad-regular/ to your project
- [ ] Step 2: Drop your IEEEtran.cls + IEEEtran.bst into the project directory
            (the template does not ship them, since IEEE recommends using a
             current copy from CTAN or the IEEE Author Tools page)
- [ ] Step 3: Verify the template compiles as-is (before any changes)
- [ ] Step 4: Replace title, authors, abstract, keywords
- [ ] Step 5: Fill section contents incrementally; compile frequently
- [ ] Step 6: Add real entries to refs.bib via the verified citation workflow
```

**Step 2 — getting `IEEEtran.cls`:**

- Download from CTAN: <https://www.ctan.org/pkg/ieeetran>
- Or from IEEE Author Tools: <https://www.ieee.org/conferences/publishing/templates.html>
- Or copy one you already have

### Compiling

```bash
latexmk -pdf main.tex            # recommended
# Or manually:
pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex
```

The template also ships with a `Makefile`. Just run `make`.

### Useful Template Macros (already defined)

| Macro | Purpose |
|-------|---------|
| `\method{}` | Method name placeholder — search-and-replace once you have a name |
| `\eg \ie \etal` | Properly-spaced abbreviations |
| `\rev{...}` | Mark first-round revisions (blue text) |
| `\revtwo{...}` | Mark second-round revisions (magenta text) |

For camera-ready, redefine the revision macros to no-ops:

```latex
\renewcommand{\rev}[1]{#1}
\renewcommand{\revtwo}[1]{#1}
```

### Template Pitfalls

| Pitfall | Solution |
|---------|----------|
| `\documentclass[conference]{IEEEtran}` | Use `[journal,letterpaper]` for TCAD/TVLSI |
| `\citet{}` / `\citep{}` | Use plain `\cite{}` (cite package, not natbib) |
| Mixing `subcaption` and `subfig` | Pick one; IEEEtran convention is `subfig` |
| Modifying `IEEEtran.cls` | Don't — breaks conference formatting |
| Forgetting to update `\markboth` | Update with your title + authors for the page header |

---

## Conference → Journal Conversion

### Workflow 3: Extending a Conference Paper to TCAD/TVLSI

A common path: extend a DAC / ICCAD / DATE / ASP-DAC paper into a TCAD journal version. IEEE policy requires the journal version to have **substantial additional content** (commonly >30% new material), and the overlap must be declared in the cover letter.

```
Conference → Journal Conversion Checklist:
- [ ] Step 1: Identify what is new in the journal version (more experiments?
            extended algorithm? new theoretical analysis? new application domain?)
- [ ] Step 2: Add a clear "extended journal version of [conf cite]" footnote
- [ ] Step 3: Re-baseline against more recent prior work
- [ ] Step 4: Add at least one of: (a) new theoretical analysis,
            (b) ablation study not in conf version, (c) extension to a new
            application/setting, (d) extended discussion + case studies
- [ ] Step 5: Expand the conference-version "Related Work" into a full
            Background and Related Work section (one combined Section II),
            adding any background/primer material the journal audience needs
- [ ] Step 6: Re-format from conference style (`IEEEtran[conference]`) to
            `IEEEtran[journal,letterpaper]`
- [ ] Step 7: Update self-citation to the conference paper (do not hide it)
- [ ] Step 8: Disclose the conference version in the cover letter with an
            explicit overlap statement
```

Common pitfalls:

- ❌ Submitting the conference paper "as-is" with only minor edits — editors will reject
- ❌ Failing to declare overlap with the conference version (required by IEEE policy)
- ❌ Keeping `\documentclass[conference]{IEEEtran}` — must change to `journal`

---

## Workflow 2: Citation Workflow (Hallucination Prevention)

**⚠️ CRITICAL**: AI-generated citations have ~40% error rate. **Never write BibTeX from memory.**

```
Citation Verification (MANDATORY for every citation):
- [ ] Step 1: Search IEEE Xplore (preferred) or DBLP / Semantic Scholar
- [ ] Step 2: Verify paper exists in 2+ sources (e.g., Xplore + DBLP)
- [ ] Step 3: Retrieve BibTeX via "Cite This → BibTeX" on Xplore, or DOI → CrossRef
- [ ] Step 4: Verify the claim you're citing actually appears in the paper
- [ ] Step 5: Add verified BibTeX to bibliography
- [ ] Step 6: If ANY step fails → mark as placeholder, inform scientist
```

| Situation | Action |
|-----------|--------|
| Found paper, got DOI, fetched BibTeX | ✅ Use the citation |
| Found paper, no DOI | ✅ Use Xplore / DBLP BibTeX |
| Paper exists but can't fetch BibTeX | ⚠️ Mark placeholder, inform scientist |
| Uncertain if paper exists | ❌ Mark `[CITATION NEEDED]`, inform scientist |
| "I think there's a paper about X" | ❌ **NEVER cite** — search first or mark placeholder |

See [references/citation-workflow-ieee.md](references/citation-workflow-ieee.md) for code, APIs, and common cases.

---

## Workflow 5: Revising After Major/Minor Revision

**The response-to-reviewers letter often determines acceptance**, and is the workflow most underestimated by first-time journal authors.

See [references/revision-workflow.md](references/revision-workflow.md) for the full workflow. High-level summary:

```
Revision Workflow:
- [ ] Step 1: Read the editor's letter carefully — identify "must-do" vs "consider"
- [ ] Step 2: Parse every reviewer comment into an atomic, numbered list
- [ ] Step 3: For each comment, decide: agree-and-fix, partial-agree-and-clarify,
            or respectfully-disagree-and-justify
- [ ] Step 4: Make manuscript changes, marking them in color (\rev{...}) or via latexdiff
- [ ] Step 5: Write a point-by-point response letter (template provided)
- [ ] Step 6: Cross-reference: every response cites a specific line/section in the revised paper
- [ ] Step 7: Re-verify all citations, including any new ones added
- [ ] Step 8: Ensure new experiments don't break old numbers
- [ ] Step 9: Submit revised manuscript + response letter + (optional) diff PDF
```

Critical rules:

1. **Quote the reviewer comment verbatim** before each response.
2. **Cite specific line numbers or section IDs** in the revised manuscript.
3. **Never argue without action** — even if you disagree, add a clarification to the paper.
4. **Use color or `\revisedtext` to highlight all changes** in the revised PDF.

A LaTeX template is provided in [templates/response-letter/](templates/response-letter/).

---

## Common Issues and Solutions

**Issue: Abstract too generic**

Delete the first sentence if it could be prepended to any paper in the area. Start with your specific contribution.

**Issue: Introduction exceeds 2 pages**

Move broader background material out of the introduction and into the unified **Background and Related Work** section (Section II). Front-load contribution bullets. For a 14-page TCAD Regular Paper, Methods should start by page 3–4. See the [Length Budget](references/writing-guide.md#length-budget-for-ieee-transactions-papers) for the full allocation across sections.

**Issue: Experiments lack explicit claims**

Add a sentence before each experiment: "This experiment tests whether [specific claim]..."

**Issue: Reviewers find the paper hard to follow**

- Add explicit signposting: "In this section, we show X"
- Use consistent terminology throughout
- Make figure captions stand alone

**Issue: Page count over the limit**

- Move proofs and large tables to an appendix or supplementary material
- Tighten the Background and Related Work section by citing surveys
- Consolidate similar tables; use `subfig` for related figures
- Eliminate filler words and hedging (see [writing-guide.md](references/writing-guide.md))

**Issue: Major Revision verdict, not sure how to respond**

See [references/revision-workflow.md](references/revision-workflow.md). The response letter is often more important than the revised paper itself.

---

## Reviewer Evaluation Criteria

TCAD/TVLSI reviewers typically score on:

| Criterion | What Reviewers Look For |
|-----------|------------------------|
| **Originality** | Novel idea / formulation / approach, not just incremental tuning |
| **Significance** | Impact on the community: design productivity, methodology, understanding |
| **Technical Soundness** | Correctness of method, completeness of evaluation |
| **Experimental Rigor** | Reproducible setup, fair baselines, multiple metrics where relevant |
| **Clarity / Presentation** | IEEEtran formatting, figure quality, English quality |
| **Reproducibility** | Configurations stated, ideally code/data release |

See [references/tcad-submission-guide.md](references/tcad-submission-guide.md) for the full checklist.

---

## References & Resources

### Reference Documents (Deep Dives)

| Document | Contents |
|----------|----------|
| [writing-guide.md](references/writing-guide.md) | Narrative principle, abstract formula, Gopen & Swan 7 principles, Perez micro-tips, word choice (Lipton, Steinhardt), figure design, common mistakes |
| [tcad-submission-guide.md](references/tcad-submission-guide.md) | TCAD-specific submission rules: page limits, EDIcs categories, cover letter, ScholarOne, camera-ready |
| [revision-workflow.md](references/revision-workflow.md) | Major/minor revision workflow, response-to-reviewers letter conventions |
| [citation-workflow-ieee.md](references/citation-workflow-ieee.md) | IEEE-style citation workflow with Xplore, DBLP, CrossRef, Semantic Scholar |
| [sources.md](references/sources.md) | External resources and bibliography |

### LaTeX Templates

Templates in `templates/`:

- **`templates/tcad-regular/`** — A complete IEEEtran journal-style starting point: `main.tex` with sectioned `\input{}` files, `refs.bib`, `Makefile`. Drop your own `IEEEtran.cls` + `IEEEtran.bst` next to `main.tex`.
- **`templates/response-letter/`** — A response-to-reviewers letter with LaTeX macros for quoting comments and cross-referencing revised sections.

See [templates/README.md](templates/README.md) for setup instructions.

### Key External Sources

**Writing Philosophy:**

- [Neel Nanda: How to Write ML Papers](https://www.alignmentforum.org/posts/eJGptPbbFPZGLpjsp/highly-opinionated-advice-on-how-to-write-ml-papers) — Narrative, "What/Why/So What"
- [Farquhar: How to Write ML Papers](https://sebastianfarquhar.com/on-research/2024/11/04/how_to_write_ml_papers/) — 5-sentence abstract
- [Gopen & Swan: Science of Scientific Writing](https://cseweb.ucsd.edu/~swanson/papers/science-of-writing.pdf) — 7 reader expectation principles
- [Lipton: Heuristics for Scientific Writing](https://www.approximatelycorrect.com/2018/01/29/heuristics-technical-scientific-writing-machine-learning-perspective/) — Word choice
- [Perez: Easy Paper Writing Tips](https://ethanperez.net/easy-paper-writing-tips/) — Micro-level clarity

**Official IEEE / TCAD:**

- [IEEE TCAD on Xplore](https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=43)
- [IEEE Author Center — Journals](https://journals.ieeeauthorcenter.ieee.org/)
- [IEEE Manuscript Templates](https://www.ieee.org/conferences/publishing/templates.html)
- [CTAN IEEEtran package](https://www.ctan.org/pkg/ieeetran)

**Citation Sources:**

- [IEEE Xplore](https://ieeexplore.ieee.org/search/searchresult.jsp)
- [ACM Digital Library](https://dl.acm.org/)
- [DBLP](https://dblp.org/)
- [CrossRef REST](https://www.crossref.org/documentation/retrieve-metadata/rest-api/)
- [Semantic Scholar API](https://api.semanticscholar.org/api-docs/)
