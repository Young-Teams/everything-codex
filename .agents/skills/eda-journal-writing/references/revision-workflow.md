# Revision Workflow and Response-to-Reviewers Letters

Nearly every TCAD paper goes through at least one round of revision. Most go through two. The **response-to-reviewers letter** is often a longer document than the revised paper itself, and it determines whether the paper is ultimately accepted.

This document covers:

1. How to read a TCAD decision letter
2. How to structure a response letter
3. How to mark changes in the revised manuscript
4. How to handle each kind of reviewer comment
5. Common mistakes that turn Major Revision into Reject

A LaTeX template for the response letter is in [../templates/response-letter/](../templates/response-letter/).

---

## 1. Reading the Decision Letter

The editor's decision letter is the **most important document** in the revision phase. Read it carefully — it tells you:

1. **The verdict** (Major Revision / Minor Revision / Reject and Resubmit / Accept with Minor)
2. **The editor's own emphasis** — what they consider the deciding issues
3. **Which reviewer comments are "must-address"** vs "consider"
4. **The deadline** — TCAD usually allows 60-90 days for Major Revision
5. **Any meta-instructions** — e.g., "the paper must be shortened by 2 pages" or "the contribution overlap with reference X must be clarified"

**Always quote the editor's letter in your response.** Address the editor's specific points first, then the individual reviewer comments.

### Editor's-Letter Categorization Pattern

When the decision arrives, run through the editor's letter and the reviews and bucket every concern into one of these categories:

| Category | Action |
|----------|--------|
| **Critical** — editor or all reviewers raise it | Must fix; spend most effort here |
| **Major** — at least one reviewer flags as decision-affecting | Must address; either fix or strongly justify |
| **Minor** — small clarifications, typos, suggestions | Fix without ceremony, mention briefly |
| **Conflicting** — reviewers disagree | Pick the technically-correct side; explain reasoning |
| **Out-of-scope** — outside paper's claims | Politely defer; promise to discuss in future work |

---

## 2. Response Letter Structure

A TCAD response letter typically has this structure:

```
1. Cover paragraph (to the editor)
   - Thank for the opportunity to revise
   - Summarize main changes in 3-5 bullets
   - Note the document's organization

2. Response to editor's letter
   - Quote each editor-level point
   - Describe your response
   - Cross-reference the relevant section / line numbers

3. Response to Reviewer 1
   - Quote each comment
   - Describe your response per comment
   - Cross-reference the manuscript

4. Response to Reviewer 2
   ...

5. (Optional) Summary of changes
   - High-level list of new sections, new figures, new experiments
```

### Tone

- **Professional and respectful**, never defensive.
- Thank each reviewer once at the start, not before every response.
- When you disagree with a reviewer, **always still add a clarification to the paper** that addresses the underlying confusion. Do not just argue.
- Avoid sycophancy ("we deeply thank the reviewer for their valuable, insightful, and excellent comment, which has tremendously improved the paper").

### Length

- Major Revision response letters in TCAD often run **10-30 pages**.
- Minor Revision response letters are usually 2-5 pages.
- Length is fine as long as it is dense; no padding.

---

## 3. The Per-Comment Response Pattern

For each individual reviewer comment, follow this 4-part pattern:

```
[COMMENT R1.3]
> [Quote the reviewer's comment verbatim, in italics or block-quote]

[ACKNOWLEDGE]
We thank the reviewer for raising this point.

[ACTION TAKEN]
- We have added a new subsection (Section III-D, p. 8, lines 12-25) that ...
- We have added Table V comparing ...
- We have updated Figure 3 to show ...

[RESULT]
With these changes, the manuscript now [resolves the concern by ...]. The new
comparison shows that our method outperforms [baseline] by 12.4% on benchmark
[X].

[OPTIONAL: DELTA EXCERPT]
For convenience, we reproduce the relevant new text here:

> [Quote the new text from the paper, indented]
```

This 4-part pattern (quote → acknowledge → action → result) makes it easy for the reviewer to verify your response in one pass. If they don't see all four parts, they may suspect you didn't really fix the issue.

### When You Disagree

If a reviewer asks for something you cannot or should not do:

```
[COMMENT R2.5]
> The authors should compare against XYZ [hypothetical baseline] which
> achieves better results on the same benchmark.

[ACKNOWLEDGE]
We thank the reviewer for the suggestion. After investigation, we believe
this comparison is not appropriate for the current submission, and we
explain our reasoning below.

[JUSTIFICATION]
XYZ targets gate-level technology mapping for FPGA architectures, whereas
the proposed method targets ASIC standard-cell placement. The two methods
operate at different levels of the EDA flow (gate mapping vs physical
placement) and on incompatible target technologies (LUT-based FPGA vs
standard-cell ASIC). A direct comparison would require porting one to the
other's target, which is itself a significant research effort and not
representative of either method's intended use.

[ACTION TAKEN (clarification, not full fix)]
To address the reviewer's underlying concern about the scope of related work,
we have added a new paragraph in Section II-B (p. 4, lines 8-19) that
explicitly delineates the boundary between FPGA technology mapping and ASIC
placement, citing XYZ as representative of the former.

[RESULT]
We hope this clarification resolves the reviewer's concern. We are happy to
add a direct empirical comparison in a future extension if the FPGA-to-ASIC
porting becomes feasible.
```

Key rule: **never refuse a comment without taking some action**. Even disagreement gets converted into a paper-level clarification.

### When the Reviewer Is Wrong

Sometimes reviewers misread the paper. Don't say "the reviewer is wrong". Instead:

```
[COMMENT R1.7]
> The proposed method runs in O(n^2), which is too slow for industrial designs.

[ACKNOWLEDGE]
We thank the reviewer for raising the question of scalability.

[ACTION TAKEN]
We realize the previous version of Section III-C may have been ambiguous on
this point. The proposed method runs in O(n log n), not O(n^2). The O(n^2)
expression in old Equation (5) referred to a hypothetical baseline (now
labeled "Baseline B" in the revised text) rather than the proposed method.
We have rewritten Section III-C (p. 7, lines 1-15) and renamed Equation (5)
as Equation (5b) to disambiguate.

[RESULT]
The proposed method's O(n log n) complexity is now explicitly stated in
Theorem 1 (p. 7) and supported by the runtime measurements in Figure 8,
which show near-linear scaling on designs from 10k to 500k cells.
```

The implicit message — "you misread the paper" — is conveyed without saying it.

---

## 4. Marking Changes in the Revised Manuscript

TCAD reviewers should be able to **find every change without re-reading the paper**. Mark changes using one of these approaches:

### Option A: Colored text (preferred)

```latex
% In the preamble:
\usepackage{xcolor}
\newcommand{\rev}[1]{\textcolor{blue}{#1}}     % first-round revisions
\newcommand{\revtwo}[1]{\textcolor{magenta}{#1}}  % second-round revisions

% In the body:
The proposed method achieves \rev{a 12.4\% reduction in metric}
compared to the baseline.
```

For larger blocks:

```latex
\rev{%
This subsection has been added in response to Reviewer 1, Comment 3, to
clarify the relationship between the proposed method and prior work on
ILP-based legalization. ...
}
```

### Option B: latexdiff (alternative)

Generate a diff PDF using `latexdiff`:

```bash
latexdiff main_v1.tex main_v2.tex > main_diff.tex
pdflatex main_diff.tex
```

Submit `main_diff.pdf` as supplementary. Use the clean `main.tex` (no color commands) as the actual manuscript.

### Option C: Both (most thorough)

Some authors use `\rev{}` in the working manuscript during revision, **and** also produce a `latexdiff` PDF for submission. The `\rev{}` macros are then redefined to no-op (`\renewcommand{\rev}[1]{#1}`) for the camera-ready version.

```latex
% For revision submission:
\newcommand{\rev}[1]{\textcolor{blue}{#1}}

% For camera-ready:
\newcommand{\rev}[1]{#1}
```

This way you can submit a colored revision PDF without removing the macros.

---

## 5. Common Mistakes That Turn Major Revision Into Reject

### Mistake 1: Ignoring a comment

The fastest way to fail revision is to silently skip a comment. **Every comment must get a response**, even if your response is "we agree and have fixed it; see line 5 of page 8".

### Mistake 2: Adding new claims that don't appear in the paper

If your response promises "we have added a new experiment showing X", and then the manuscript doesn't actually show X, the reviewer will reject. **The paper and the letter must match.**

### Mistake 3: Hiding behind page limits

❌ "We agree this experiment would be valuable but we cannot add it due to page limits."

This is rarely acceptable. Better:

✅ "Per the reviewer's request, we have added the experiment as Table VII (p. 14). To accommodate it, we moved the previous Table IV to the supplementary material and condensed the discussion in Section IV-B."

### Mistake 4: Arguing without action

If you disagree with a reviewer, you still need to add a paper-level clarification (see above). Pure rebuttal without any change to the manuscript signals that you didn't take the comment seriously.

### Mistake 5: Reformatting without resubstantiating

Major revisions are about **new evidence**, not better prose. If the editor said "please add empirical comparison to method X", a polished rewrite of the existing experiments will not save the paper.

### Mistake 6: Not re-checking old numbers

If you add a new experiment or change the algorithm in response to one reviewer, **re-run all old experiments**. Reviewers will check whether numbers in Table III match across versions. A single inconsistency triggers suspicion.

### Mistake 7: Adding self-citation that breaks blind review

If TCAD is double-blind this year, **do not add citations to your own newer work** that would reveal identity. Cite them as `[anonymous] [our prior work, citation withheld for review]`.

### Mistake 8: Letting the response letter contradict the manuscript

If the response says "we now use setup X" but the paper says "we use setup Y", the editor will see this immediately. Always cross-check.

### Mistake 9: Forgetting to re-verify citations

When adding new references for the revision, **re-verify them** using the citation workflow. Hallucinated citations are a common cause of revision-stage rejection.

### Mistake 10: Submitting late without contact

If the 90-day deadline is going to be missed, **contact the editor in advance** and request an extension. Editors usually grant a short extension if asked; they will reject silently-late revisions.

---

## 6. Workflow Checklist

```
Major Revision Workflow:
- [ ] Step 1: Receive decision letter and reviews
- [ ] Step 2: Extract every individual comment into a numbered list
            (R1.1, R1.2, R2.1, ...)
- [ ] Step 3: Categorize each as Critical / Major / Minor / Conflicting / OoS
- [ ] Step 4: Draft response plan for each (agree-and-fix /
            partial-agree-clarify / respectfully-disagree-clarify)
- [ ] Step 5: Make manuscript changes, marking with \rev{} or color
- [ ] Step 6: Re-run all experiments that might be affected
- [ ] Step 7: Verify any new citations programmatically
- [ ] Step 8: Re-compile and check page count + overlength
- [ ] Step 9: Write the response letter using the 4-part per-comment pattern
- [ ] Step 10: Cross-reference: every response cites a specific section / line
- [ ] Step 11: Sanity-check that response letter and manuscript agree
- [ ] Step 12: Have a co-author or colleague read both
- [ ] Step 13: Generate diff PDF (latexdiff) as supplementary
- [ ] Step 14: Submit via ScholarOne with: revised manuscript + response letter
            + diff PDF
```

---

## 7. Sample Response Letter Opening

```
Editor and Reviewers of IEEE TCAD,

We sincerely thank the editor and the three reviewers for their detailed
and constructive comments on our manuscript "<TITLE>" (Manuscript ID
TCAD-2024-XXXX). The reviews have substantially strengthened the paper.

The main changes in this revision are:

(i)   We have added a new section (Section IV-D) presenting a formal
      complexity analysis of the proposed algorithm, in response to
      Reviewer 1, Comment 2 and Reviewer 3, Comment 1.

(ii)  We have added a new experimental subsection (Section V-C) comparing
      against two additional recent baselines, [25] and [26], on the
      benchmarks used in the paper, in response to Reviewer 2,
      Comments 1 and 4.

(iii) We have substantially revised Section II to better contextualize
      our contribution within prior work on placement legalization, in
      response to Reviewer 1, Comment 1 and Reviewer 2, Comment 2.

(iv)  We have corrected the algorithmic-complexity discussion in Section
      III-C, which was incorrect in the original submission, as
      Reviewer 1, Comment 3 helpfully pointed out.

(v)   We have fixed all typos and notation inconsistencies flagged by
      Reviewer 3.

Below, we respond to each individual comment in turn. Reviewer comments
are reproduced in italics; our responses follow in regular type. New text
in the revised manuscript is marked in blue.

[BEGIN RESPONSE TO EDITOR]
...
[BEGIN RESPONSE TO REVIEWER 1]
...
```

A full LaTeX template implementing this structure (with macros for `\reviewercomment{}`, `\response{}`, `\paperref{section,line}`) is in [../templates/response-letter/](../templates/response-letter/).
