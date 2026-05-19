# IEEE TCAD Submission Guide

This document collects the practical submission requirements for **IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (TCAD)** and its closest siblings (TVLSI, TODAES, ESL). All numbers below are derived from the official IEEE author center and IEEE-CEDA author information pages and should be re-verified before submission, since IEEE policies and overlength fees occasionally change.

**Official sources to re-check:**

- <https://journals.ieeeauthorcenter.ieee.org/>
- <https://ieee-ceda.org/publications/ieee-transactions-computer-aided-design-tcad>
- <https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=43>

---

## TCAD at a Glance

| Item | Value |
|------|-------|
| Manuscript system | ScholarOne Manuscripts |
| Article types | Regular Paper, Brief Contribution, Survey, Special Section Paper |
| Document class | `IEEEtran` with `[journal,letterpaper]` options |
| Column layout | Two-column |
| Body font | 10 pt (set by IEEEtran journal mode) |
| Page size | US Letter (8.5" × 11") |
| Regular Paper length | Aim for ≤ 14 pages including figures, tables, references, biographies |
| Overlength | Pages beyond the 14-page target incur per-page charges (rate set by IEEE; check author center) |
| Blind review | Single-blind by default; some special issues / years run double-blind — **always verify per-year** |
| Review rounds | Typically 2-3 (Major Revision → Minor Revision → Accept) |
| Required additional sections | Acknowledgments (if applicable); Author Biographies in camera-ready (with photos) |
| Supplementary material | Allowed (data, code, extended proofs); referenced from the main text |

---

## Submission Phase Checklist

Use this list before you press "Submit" in ScholarOne.

### Manuscript Content

- [ ] Title is descriptive and contains the key technique + the problem
- [ ] Abstract is 200-250 words and contains at least one concrete quantitative result
- [ ] IEEE keywords are chosen from the official taxonomy when possible
- [ ] Introduction states the contribution as a bulleted list (3-5 bullets)
- [ ] All figures are vector (PDF/EPS/TikZ) and readable in black-and-white
- [ ] All tables use `booktabs` rules and have captions **above** the table
- [ ] All figures have captions **below** the figure
- [ ] All algorithms use `algorithm` + `algorithmic` packages
- [ ] Experimental section describes the setup at the level of detail required for reproducibility in your sub-area (tools, configurations, datasets, etc. — the domain scientist knows the local conventions)
- [ ] Baselines and metrics follow the conventions of the relevant TCAD sub-community
- [ ] All numeric claims in the abstract are reproduced in the experimental section with the same numbers
- [ ] All citations are programmatically verified (see citation-workflow-ieee.md)
- [ ] All BibTeX entries have DOI or arXiv ID when available

### Formatting

- [ ] `\documentclass[journal,letterpaper]{IEEEtran}` is the first non-comment line
- [ ] `\bibliographystyle{IEEEtran}` is used
- [ ] All references use `\cite{}` (not `\citet/\citep`)
- [ ] `\markboth{<journal name>}{<author et al.>: <short title>}` is set
- [ ] No `[twocolumn]`, `[10pt]`, or similar options that override IEEEtran defaults
- [ ] Compiles cleanly with `pdflatex` + `bibtex` + `pdflatex` + `pdflatex` with no missing references / no undefined citations
- [ ] No "Overfull \hbox" warnings exceeding 5pt
- [ ] No "LaTeX Warning: Reference XYZ undefined"
- [ ] Page count is at or below 14 (or you have explicit budget for overlength fees)

### Blind Review Hygiene (if double-blind year)

- [ ] Authors removed from title page
- [ ] Affiliations removed from title page
- [ ] `\thanks{}` blocks with funding/affiliation commented out
- [ ] Self-citations rephrased to third person ("Smith et al. [12]" → "Prior work [12]")
- [ ] Acknowledgments section removed or anonymized
- [ ] No `\href{}` to personal homepages or GitHub repos that reveal identity
- [ ] PDF metadata (Title, Author, Producer) does not reveal identity — use `\hypersetup{pdfauthor={}}`

### Single-Blind Round Hygiene (most common case)

- [ ] Author block is complete with `\IEEEmembership{...}` for each author
- [ ] Corresponding author email is in a `\thanks{}` block
- [ ] All affiliations are present and current
- [ ] Funding sources are credited in `\thanks{}` or Acknowledgments

### Supplementary Material (optional but recommended)

- [ ] Code repository link (or anonymous mirror if double-blind)
- [ ] Data / benchmark generation scripts
- [ ] Extended proofs / additional ablations
- [ ] Reproducibility statement near the end of the paper

### ScholarOne Submission Form

- [ ] Cover letter explaining the contribution in 3-4 sentences
- [ ] List of suggested reviewers (TCAD often asks for 3-5)
- [ ] List of non-preferred reviewers (only if you have a genuine conflict)
- [ ] Disclosure of prior conference version (if extending DAC/ICCAD/DATE etc.), with explicit overlap statement (e.g., "This manuscript extends our DAC 2024 paper [XX] with three new contributions: ...")
- [ ] Selected the correct article type (Regular vs Brief)
- [ ] Selected the correct EDIcs (TCAD's editorial categories)

---

## TCAD EDIcs (Editorial Categories)

TCAD organizes submissions into EDIcs categories. Select carefully — the wrong EDIcs sends your paper to the wrong editor and reviewers. Common categories:

- Logic Synthesis
- Physical Design (Placement, Routing, Floorplanning)
- Timing Analysis and Signoff
- Verification (Formal, Simulation, Emulation)
- High-Level Synthesis
- System-Level Design and ESL
- Hardware Security
- Machine Learning for CAD
- Test, Debug, and Reliability
- Emerging Technologies (Quantum, Neuromorphic, Photonics)
- Low-Power Design
- Analog/Mixed-Signal CAD

Pick the one closest to your contribution. If you span two, list a primary and secondary.

---

## Cover Letter Template (TCAD)

```
Dear Editor-in-Chief,

We are pleased to submit our manuscript entitled "<TITLE>" for consideration
as a Regular Paper in IEEE Transactions on Computer-Aided Design of Integrated
Circuits and Systems.

In this work, we propose <ONE-SENTENCE CONTRIBUTION>. Our key results are:
(1) <headline result 1 with numbers>,
(2) <headline result 2 with numbers>,
(3) <headline result 3 with numbers>.

The work falls within the "<EDIcs CATEGORY>" editorial category.

[If extending a conference paper:]
A preliminary version of this work appeared in <CONFERENCE> [<CITE>].
The journal version extends that work by:
  (a) <new theoretical analysis / new experiments / new application / etc.>,
  (b) ...,
  (c) ....
We estimate the overlap with the conference version at approximately <X>%.

We confirm that this manuscript has not been published elsewhere and is not
under consideration by any other journal.

Sincerely,
<Corresponding author name and affiliation>
```

---

## Common Reasons TCAD Papers Get Rejected

Drawn from the IEEE-CEDA editor blog posts and informal community knowledge:

1. **Setup not reproducible** — tools, configurations, or datasets not stated in enough detail for the sub-community.
2. **Evaluation does not follow the sub-area's conventions** — wrong or missing baselines, single-metric where multiple matter, evaluation on non-representative inputs.
3. **No comparison to recent prior work** — only old baselines (>5 years).
4. **Conference-paper-as-is** — insufficient extension over the prior conference version.
5. **Hallucinated citations** — desk-reject risk.
6. **Wrong document class** — `[conference]` instead of `[journal]`, or non-IEEE template.
7. **Overlength without justification** — papers running 20+ pages without dense content.
8. **Limited novelty** — incremental improvement of one prior method without insight.
9. **Poor English / unclear structure** — the contribution may be there, but reviewers cannot extract it.
10. **Wrong EDIcs category / wrong venue** — paper does not align with TCAD's scope (consider TVLSI / TODAES / a conference instead).

Note: what counts as "standard" baselines, benchmarks, tool versions, etc. is sub-area-specific. The domain scientist is the source of truth for what reviewers in your sub-community expect to see.

---

## Decision Letter Codes (TCAD)

When you receive a decision, the editor's letter will be one of:

| Decision | Meaning | Typical action |
|----------|---------|----------------|
| **Accept** | Almost never on first round | Camera-ready preparation |
| **Accept with Minor Revision** | Small fixes needed | 1-2 month turnaround |
| **Major Revision (Reject and Resubmit)** | Significant changes required, new round of review | 2-4 month turnaround |
| **Reject** | Paper not suitable in current form | Substantial rework or different venue |

Even "Reject" decisions in EDA journals sometimes invite resubmission as a new manuscript. Always read the editor's letter fully.

---

## Camera-Ready (After Accept)

When your paper is accepted, the camera-ready phase adds requirements that the review version did not:

- **Author Biographies** with high-resolution photo (300 dpi headshot, color), 60-150 words per author, IEEE biography style. Use the `\IEEEbiographynophoto{...}` or `\IEEEbiography[...]{...}` macros (already supported by `IEEEtran.cls`).
- **Final author list and affiliations** — no longer anonymized
- **Funding acknowledgments** in Acknowledgments section
- **All `\thanks{}` blocks** filled in
- **Copyright statement** (IEEE provides this; do not change)
- **ORCID iDs** for each author (recommended)
- **DOI for any cited preprints**, replaced with published DOI if available

```latex
% Example author biography (used in camera-ready only)
\begin{IEEEbiography}[{\includegraphics[width=1in,height=1.25in,clip,keepaspectratio]{figs/bio_alice.jpg}}]
{Alice Smith}
(M'18) received the B.S. and Ph.D. degrees in Electrical Engineering from ...
She is currently an Assistant Professor at ...
Her research interests include logic synthesis, machine learning for EDA, and ...
\end{IEEEbiography}
```

---

## Closely Related Journals (Quick Comparison)

| Journal | Scope | Length | Notes |
|---------|-------|--------|-------|
| **TCAD** | EDA algorithms, design methodology, CAD tools | ≤14 pages | The flagship EDA journal |
| **TVLSI** | VLSI implementation, circuits, architectures | ≤10-12 pages | Closer to circuits/architecture than EDA tools |
| **TODAES** | Design automation, methodology | No strict limit (~25) | Slower review; ACM journal |
| **ESL** | Short novel results | 4 pages strict | "Letters" — for compact contributions |
| **TC** (Trans. on Computers) | Computer architecture, systems | ≤14 pages | Architecture-leaning |
| **TPDS** (Trans. on Parallel & Distributed Systems) | Parallel/distributed | ≤14 pages | Systems-leaning |

Choosing between them:

- **TCAD**: your contribution is an algorithm, methodology, or tool for EDA.
- **TVLSI**: your contribution is a circuit, architecture, or chip-level implementation.
- **TODAES**: your contribution is a longer system-level design methodology paper.
- **ESL**: a small, sharp novel result.
- **TC / TPDS**: your contribution is more about computer architecture or parallel systems than EDA.
