# Paper Writing Philosophy & Best Practices

This reference compiles writing advice from prominent researchers — Neel Nanda, Andrej Karpathy, Sebastian Farquhar, George Gopen & Judith Swan, Zachary Lipton, Ethan Perez, Jacob Steinhardt — and adapts the recommendations for an IEEE Transactions audience (TCAD, TVLSI, TODAES, ESL).

The advice is mostly venue-agnostic. The IEEE-specific notes (numeric citations, two-column layout, figure/table caption placement) are flagged where they matter.

---

## Contents

- [The Narrative Principle](#the-narrative-principle)
- [Time Allocation](#time-allocation)
- [Abstract Writing Formula](#abstract-writing-formula)
- [Introduction Structure](#introduction-structure)
- [Length Budget for IEEE Transactions Papers](#length-budget-for-ieee-transactions-papers)
- [Sentence-Level Clarity (Gopen & Swan)](#sentence-level-clarity-gopen--swan)
- [Micro-Level Writing Tips (Perez)](#micro-level-writing-tips-perez)
- [Word Choice and Precision (Lipton, Steinhardt)](#word-choice-and-precision-lipton-steinhardt)
- [Mathematical Writing](#mathematical-writing)
- [Figure Design](#figure-design)
- [IEEE Transactions Voice and Conventions](#ieee-transactions-voice-and-conventions)
- [Common Mistakes to Avoid](#common-mistakes-to-avoid)
- [Pre-Submission Checklist](#pre-submission-checklist)

---

## The Narrative Principle

### From Neel Nanda

> "A paper is a short, rigorous, evidence-based technical story with a takeaway readers care about."

The narrative rests on three pillars that must be crystal clear by the end of your introduction:

**The "What"**: One to three specific novel claims fitting within a cohesive theme. Vague contributions like "we study X" fail immediately — reviewers need precise, falsifiable claims.

**The "Why"**: Rigorous empirical evidence that convincingly supports those claims, including strong baselines honestly tuned and experiments that distinguish between competing hypotheses rather than merely showing "decent results."

**The "So What"**: Why readers should care, connecting your contribution to problems the community recognizes as important.

### From Andrej Karpathy

> "A paper is not a random collection of experiments you report on. The paper sells a single thing that was not obvious or present before. The entire paper is organized around this core contribution with surgical precision."

This applies whether you're presenting a new algorithm, a new framework, a new theoretical result, or improved understanding of existing methods — originality does not necessarily require an entirely new method.

**Practical Implication**: If you cannot state your contribution in one sentence, you don't yet have a paper. Everything else — experiments, related work, discussion — exists only to support that core claim.

---

## Time Allocation

### From Neel Nanda

Spend approximately **the same amount of time** on each of:

1. The abstract
2. The introduction
3. The figures
4. Everything else combined

Most reviewers form preliminary judgments before reaching your methods section. Readers encounter your paper in a predictable pattern: **title → abstract → introduction → figures → maybe the rest.**

### Reviewer Reading Patterns

Studies of reviewer behavior show:

- Abstract is read 100% of the time
- Introduction is skimmed by 90%+ of reviewers
- Figures are examined before methods by most reviewers
- Full methods are read only if interest is established

**Implication**: Front-load your paper's value. Don't bury the contribution.

---

## Abstract Writing Formula

### Sebastian Farquhar's 5-Sentence Formula

1. **What you achieved**: "We introduce...", "We propose...", "We demonstrate..."
2. **Why this is hard and important**
3. **How you do it** (with specialist keywords for discoverability — search engines and Xplore both depend on this)
4. **What evidence you have**
5. **Your most remarkable number/result**

### Example (Good Abstract — generic shape)

```
We introduce a framework for [problem] that addresses [specific limitation
of prior approaches]. [What]
The problem is hard because [concrete reason], and important because
[concrete consequence for the community]. [Why hard/important]
Our approach combines [technique A] with [technique B] under a [novel
formulation], which we call [method name]. [How with keywords]
We evaluate on [benchmarks the project actually uses] and compare against
[the strongest published baselines in the area]. [Evidence]
Compared to the previous state of the art, our method achieves [headline
number, with units], a [N%] improvement. [Remarkable result]
```

### What to Avoid

From Zachary Lipton: "If the first sentence can be pre-pended to any paper in the area, delete it."

**Delete these openings**:

- "The continued scaling of integrated circuits has become a critical challenge..."
- "Large language models have achieved remarkable success..."
- "In recent years, [field] has..."

**Start with your specific contribution instead.**

---

## Introduction Structure

### Requirements (for IEEEtran two-column journal layout)

IEEE Transactions papers (TCAD, TVLSI) target ~14 pages — significantly longer than typical ML conference papers (8–9 pages). Section proportions scale accordingly: a TCAD introduction can run a full 1.5–2 pages, where an ICML/NeurIPS intro would be half that.

- **1.5–2 pages** in two-column IEEEtran journal format (≈ 12–18% of the 14-page budget)
- **Methods/Approach should start by page 3–4**
- Must include a **2–4 bullet contribution list** (each 1–3 lines in two-column format)
- For shorter venues (IEEE ESL is 4 pages total), compress the introduction to ~½ page

### Structure Template

```
1. Opening Hook (2-3 sentences)
   - State the problem your paper addresses
   - Why it matters

2. Background/Challenge (1 paragraph)
   - What makes this problem hard?
   - What have others tried? Why is it insufficient?

3. Your Approach (1 paragraph)
   - What do you do differently?
   - Key insight that enables your contribution

4. Contribution Bullets (2-4 items)
   - Be specific and falsifiable
   - Each bullet: 1-3 lines maximum (two-column format)

5. Results Preview (2-3 sentences)
   - Most impressive numbers
   - Scope of evaluation

6. Paper Organization (1-2 sentences)
   - "The rest of this paper is organized as follows. Section II..."
```

### Contribution Bullets: Good vs Bad

**Good:**

- We prove that *X* converges in *O(n log n)* under assumption *Y*
- We introduce *Z*, a framework that reduces *metric* by *40%* on *benchmark C*
- We demonstrate that *A* outperforms *B* by *15%* on *benchmark C*

**Bad:**

- We study the problem of X *(not a contribution)*
- We provide extensive experiments *(too vague)*
- We make several contributions to the field *(says nothing)*

---

## Length Budget for IEEE Transactions Papers

IEEE Transactions journals are longer than typical ML conferences, and the section proportions shift accordingly. The targets below assume a **TCAD/TVLSI Regular Paper at the 14-page mark** (TCAD's target before overlength fees). Scale proportionally for TVLSI (~10–12 pages) and aggressively for ESL (4 pages strict).

### Recommended Page Allocation (14-page TCAD Regular Paper)

| Section | Pages | % of paper | Notes |
|---------|-------|------------|-------|
| Title block + Abstract + Keywords | 0.25 | ~2% | Set by IEEEtran; abstract 200–250 words |
| **Introduction** | **1.5 – 2** | **11–14%** | Including contribution bullets and paper-organization sentence |
| Background and Related Work | 1.5 – 2 | 11–14% | **One combined Section II.** Title it "Background and Related Work" (or just "Background", or just "Related Work" — pick one). If you use subsections, group them **by topic / approach**, not by "Background" vs. "Related Work". Do **not** split into two peer top-level sections. |
| Proposed Method | 3 – 4 | 21–29% | The technical core; includes algorithm boxes, equations, complexity |
| Experimental Setup + Results | 3 – 4 | 21–29% | Setup, main table(s), ablations, optional case study |
| Discussion / Limitations | 0.5 – 1 | 4–7% | Optional but encouraged for TCAD |
| Conclusion | 0.25 – 0.5 | 2–4% | Two short paragraphs is enough |
| References | 1 – 1.5 | 7–11% | 30–60 entries typical; doesn't count toward page limit at some venues but does at TCAD |
| (Camera-ready only) Author Bios | 0.5 | — | Added after acceptance |

### What Page Should X Be On?

A rough check while drafting:

| Where you are | Should be at page... |
|---------------|----------------------|
| End of Abstract | Top of column 1 of page 1 |
| End of Introduction | Page 2 or top of page 3 |
| End of Background / Related Work | Page 4 or so |
| Start of Proposed Method | Page 3–4 |
| Start of Experiments | Page 7–9 |
| Start of References | Page 12–13 |

If your method section starts later than page 4, your introduction or background is over-budget. If experiments start earlier than page 7, your method is probably under-developed for a journal paper.

### Why The Proportions Differ From ML Conferences

ML conferences (NeurIPS, ICML at 8–9 pages) require an *introduction ≤ 1 page* and *methods by page 2*. That is correct for those venues — they assume reviewers are already deep in the area. IEEE Transactions papers serve a wider audience that includes industry practitioners and adjacent academic communities, so:

- **Background and Related Work get more space** — TCAD reviewers expect a deeper survey, not just the closest five papers.
- **Method sections are more detailed** — including pseudocode, complexity analysis, and implementation notes that a conference paper would push to an appendix.
- **Experimental sections include more ablations and case studies** — journal reviewers expect a more complete evaluation than a conference paper.

This is also why a 14-page TCAD paper takes substantially longer to write than a 9-page NeurIPS paper — there's roughly 50% more content to produce.

### Length Management

If you are over the 14-page target:

1. **Move proofs and large tables to supplementary material** (IEEEtran journals accept supplementary).
2. **Tighten Related Work** by citing surveys instead of multiple individual papers.
3. **Consolidate similar experimental tables** into one with multiple columns.
4. **Use `subfig` to combine related figures** into one float.
5. **Tighten prose** — see [Micro-Level Writing Tips](#micro-level-writing-tips-perez) below. Common cuts:
   - "in order to" → "to"
   - "it is important to note that" → delete
   - "we performed an analysis" → "we analyzed"

If you are well under the page limit (say, 10 pages for a Regular Paper), consider whether you have enough material for a journal submission rather than a conference paper, or expand:

1. **Add a case study** showing your method on a realistic problem with deep analysis.
2. **Add an ablation table** decomposing your contribution.
3. **Expand limitations and threats to validity**.
4. **Add a theoretical analysis** if applicable.

---

## Sentence-Level Clarity (Gopen & Swan)

The seminal 1990 paper by George Gopen and Judith Swan, *"The Science of Scientific Writing,"* establishes that **readers have structural expectations** about where information appears in prose. Violating these expectations forces readers to spend energy on structure rather than content.

> "If the reader is to grasp what the writer means, the writer must understand what the reader needs."

### The 7 Principles of Reader Expectations

**Principle 1: Subject-Verb Proximity**

Keep grammatical subject and verb close together. Anything intervening reads as interruption of lesser importance.

**Weak**: "The framework, which was implemented in Python and benchmarked against three baselines under identical hardware conditions, achieves state-of-the-art accuracy."

**Strong**: "The framework achieves state-of-the-art accuracy when benchmarked against three baselines under identical hardware conditions."

**Principle 2: Stress Position (Save the Best for Last)**

Readers naturally emphasize the **last words of a sentence**. Place your most important information there.

**Weak**: "Accuracy improves by 15% when using the proposed mechanism."

**Strong**: "When using the proposed mechanism, accuracy improves by **15%**."

**Principle 3: Topic Position (First Things First)**

The beginning of a sentence establishes perspective. Put the "whose story" element first — readers expect the sentence to be about whoever shows up first.

**Weak**: "A novel attention mechanism that computes alignment scores is introduced."

**Strong**: "To address the alignment problem, we introduce a novel attention mechanism."

**Principle 4: Old Information Before New**

Put familiar information in the topic position for backward linkage; put new information in the stress position for emphasis.

**Weak**: "Sparse attention was introduced by Child et al. The quadratic complexity of standard attention motivates this work."

**Strong**: "Standard attention has quadratic complexity. To address this, Child et al. introduced sparse attention."

**Principle 5: One Unit, One Function**

Each unit of discourse (sentence, paragraph, section) should serve a single function. If you have two points, use two units.

**Principle 6: Articulate Action in the Verb**

Express the action of each sentence in its verb, not in nominalized nouns.

**Weak**: "We performed an analysis of the results" *(nominalization)*

**Strong**: "We analyzed the results" *(action in verb)*

**Principle 7: Context Before New Information**

Provide context before asking the reader to consider anything new. This applies at all levels — sentence, paragraph, section.

**Weak**: "Equation 3 shows that convergence is guaranteed when the learning rate satisfies..."

**Strong**: "For convergence to be guaranteed, the learning rate must satisfy the condition in Equation 3..."

### Summary Table

| Principle | Rule | Mnemonic |
|-----------|------|----------|
| Subject-Verb Proximity | Keep subject and verb close | "Don't interrupt yourself" |
| Stress Position | Emphasis at sentence end | "Save the best for last" |
| Topic Position | Context at sentence start | "First things first" |
| Old Before New | Familiar → unfamiliar | "Build on known ground" |
| One Unit, One Function | Each paragraph = one point | "One idea per container" |
| Action in Verb | Use verbs, not nominalizations | "Verbs do, nouns sit" |
| Context Before New | Explain before presenting | "Set the stage first" |

---

## Micro-Level Writing Tips (Perez)

These practical micro-level tips from Ethan Perez improve clarity at the sentence and word level.

### Pronoun Management

**Minimize pronouns** ("this," "it," "these," "that"). When pronouns are necessary, use them as adjectives paired with a noun:

**Weak**: "This shows that the framework converges."

**Strong**: "This result shows that the framework converges."

**Weak**: "It improves runtime."

**Strong**: "This modification improves runtime."

### Verb Placement

Position verbs early in sentences for better parsing:

**Weak**: "The model, after being trained and fine-tuned, updates the parameters."

**Strong**: "The model updates the parameters after training and fine-tuning."

### Apostrophe Unfolding

Transform possessive constructions when sentences feel awkward:

**Original**: "X's Y" → **Unfolded**: "The Y of X"

**Before**: "The model's accuracy on the test set"

**After**: "The accuracy of the model on the test set"

### Words to Eliminate

Delete these filler words in almost all cases:

- "actually"
- "a bit"
- "fortunately" / "unfortunately"
- "very" / "really"
- "quite"
- "basically"
- "essentially"
- Excessive connectives ("however," "moreover," "furthermore" when not needed)

### Sentence Construction Rules

1. **One idea per sentence** — if you struggle to express an idea in one sentence, it needs two
2. **No repeated sounds** — avoid similar-sounding words in the same sentence
3. **Every sentence adds information** — delete sentences that merely restate
4. **Active voice by default** — specify the actor ("We find..." not "It is found...")
5. **Expand contractions** — "don't" → "do not" for formality

### Paragraph Architecture

- **First sentence**: state the point clearly
- **Middle sentences**: support with evidence
- **Last sentence**: reinforce or transition

Don't bury key information in the middle of paragraphs.

---

## Word Choice and Precision (Lipton, Steinhardt)

### From Zachary Lipton

**Eliminate hedging** unless genuine uncertainty exists:

- Drop "may" and "can" unless necessary
- "provides *very* tight approximation" signals insecurity
- "provides tight approximation" is confident

**Avoid vacuous intensifiers**:

- Delete: "very", "extremely", "highly", "significantly" (unless statistical)
- These words signal insecurity, not strength

### From Jacob Steinhardt

**Precision over brevity**: Replace vague terms with specific ones.

| Vague | Specific |
|-------|----------|
| performance | accuracy, latency, throughput, runtime |
| improves | increases accuracy by X%, reduces latency by Y |
| large | 1B parameters, 100M tokens, 250k gates |
| fast | 3× faster, 50 ms latency |
| good results | 92% accuracy, 0.85 F1, 12% reduction |

**Consistent terminology**: Referring to the same concept with different terms creates confusion.

**Choose one and stick with it**:

- "model" vs "network" vs "architecture"
- "training" vs "learning" vs "optimization"
- "sample" vs "example" vs "instance"
- "framework" vs "tool" vs "system"

### Vocabulary Signaling

Words signaling incremental work feel weaker than words signaling a contribution:

- Replace "combine," "modify," "expand," "extend" with "develop," "propose," "introduce" — when accurate
- "We combine X and Y" sounds like you stapled two existing ideas together
- "We develop a method that leverages X for Y" sounds like genuine contribution

Use the stronger verbs only when they reflect reality. If the work genuinely is an extension, "extend" is fine — but reframe so the bullet captures *what is novel about the extension*, not the act of extending.

---

## Mathematical Writing

### General Principles

1. **State all assumptions formally** before theorems
2. **Provide intuitive explanations** alongside proofs
3. **Use consistent notation** throughout the paper
4. **Define symbols at first use**
5. **Number equations only if referenced** — unreferenced equations clutter

### Notation Conventions

```latex
% Scalars: lowercase italic
$x$, $y$, $\alpha$, $\beta$

% Vectors: lowercase bold
$\mathbf{x}$, $\mathbf{v}$

% Matrices: uppercase bold
$\mathbf{W}$, $\mathbf{X}$

% Sets: uppercase calligraphic
$\mathcal{X}$, $\mathcal{D}$

% Functions: roman for named functions
$\mathrm{softmax}$, $\mathrm{ReLU}$, $\mathrm{eval}$
```

### Units in IEEE Style

- Always include units after numbers: `12.4\,$\mu$s`, `1.1\,V`, `45\,nm`
- Use `\,` for a thin space between number and unit
- Use `\(\times\)` (not the letter `x`) for "times": `1.8\(\times\)`
- Use `{,}` for the thousands separator in math mode: `12{,}345`

---

## Figure Design

### Design Principles

1. **Figure 1 is crucial** — often the first thing readers examine after the abstract
2. **Self-contained captions** — reader should understand the figure without main text
3. **No title inside the figure** — the caption serves this function
4. **Vector graphics** — PDF/EPS/TikZ for plots, PNG (≥300 DPI) only for photographs
5. **Captions belong below figures** in IEEEtran; **above tables**. Do not swap them.

### Accessibility Requirements

8% of men have color vision deficiency. Figures must work for them.

**Solutions**:

- Use colorblind-safe palettes: Okabe-Ito or Paul Tol
- Avoid red-green combinations
- Verify figures work in grayscale
- Use different line styles (solid, dashed, dotted) in addition to colors

### Tools

```python
# SciencePlots: Publication-ready styles, including an IEEE preset
import matplotlib.pyplot as plt
plt.style.use(['science', 'ieee'])

# Or for a Nature-style
plt.style.use(['science', 'nature'])
```

For diagrams in the paper itself, **prefer TikZ** over external raster images — TikZ scales cleanly in two-column IEEEtran and integrates with the document's fonts.

---

## IEEE Transactions Voice and Conventions

This section covers the IEEE-specific layer that the general principles above do not cover.

### Citation Style: Numeric, Not Author-Year

IEEEtran journals use numeric citations through the `cite` package:

```latex
\usepackage{cite}
% ...
prior work \cite{smith2024} has shown that ...
several methods \cite{smith2024, jones2023, lee2022} address this problem
```

The `cite` package automatically collapses ranges: `\cite{a,b,c,d}` → `[1]–[4]`.

### Don't Use Citations as Nouns

| ❌ Wrong | ✅ Right |
|---------|---------|
| "[12] proposed..." | "Smith et al. [12] proposed..." |
| "As shown in [5]..." | "As shown by Jones et al. [5]..." |
| "[7], [8], [9] explored..." | "Prior work [7]–[9] has explored..." |

### Two-Column Tables and Figures

In IEEEtran two-column layout:

- `\begin{figure}` / `\begin{table}` → single column width (`\columnwidth`)
- `\begin{figure*}` / `\begin{table*}` → spans both columns (`\textwidth`)
- Place floats with `[!t]` (top of column/page) for most cases

### Tables (booktabs convention)

```latex
\begin{table}[!t]
\caption{Comparison of methods on benchmark X}
\label{tab:results}
\centering
\begin{tabular}{lcc}
\toprule
Method & Metric 1 $\uparrow$ & Metric 2 $\downarrow$ \\
\midrule
Baseline & 85.2 & 45 \\
\textbf{Ours} & \textbf{92.1} & \textbf{38} \\
\bottomrule
\end{tabular}
\end{table}
```

**Conventions:**

- Caption **above** the table (IEEE rule)
- Use `\toprule`, `\midrule`, `\bottomrule` from `booktabs`
- Bold the best value per metric
- Use `↑` / `↓` to indicate metric direction
- Use the same number of decimal places throughout the column

### Tone

IEEE journal prose is typically **methodical and direct**, but the exact register varies by sub-community. The hard rules are:

- Be quantitative whenever you can — "12.4% improvement" beats "better"
- Eliminate hedging when reporting concrete numbers
- Use consistent terminology for the same concept
- State assumptions before conclusions

Beyond that, write in the voice that fits your sub-community. Cross-disciplinary work (e.g., LLM-driven EDA, ML-for-CAD) freely uses vocabulary from both areas; that's fine as long as terms are defined at first use.

### Acronyms

Define each acronym at first use:

> "We evaluate using static timing analysis (STA) at the post-route stage."

Some acronyms are universally known in an IEEE Transactions audience and need no definition: CMOS, RTL, ASIC, FPGA, CPU, GPU, AI, LLM, ML.

---

## Common Mistakes to Avoid

### Structure Mistakes

| Mistake | Solution |
|---------|----------|
| Introduction too long (>2 pages in 14-page TCAD) | Move background material out of the intro and into the unified Background and Related Work section (Section II); trim motivation |
| Background and Related Work split into two peer top-level sections | Merge into a single Section II under one name ("Background and Related Work", "Background", or "Related Work"); if you keep subsections, group them by topic/approach, not by "Background" vs. "Related Work" |
| Methods buried (after page 4) | Front-load contribution, tighten background |
| Missing contribution bullets | Add 2-4 specific, falsifiable claims |
| Experiments without explicit claims | State what each experiment tests |

### Writing Mistakes

| Mistake | Solution |
|---------|----------|
| Generic abstract opening | Start with your specific contribution |
| Inconsistent terminology | Choose one term per concept |
| Passive voice overuse | Use active voice: "We show" not "It is shown" |
| Hedging everywhere | Be confident unless genuinely uncertain |
| Long sentences (>30 words) | Split; non-native English readers will thank you |

### Figure / Table Mistakes

| Mistake | Solution |
|---------|----------|
| Raster graphics for plots | Use vector (PDF/EPS/TikZ) |
| Red-green color scheme | Use colorblind-safe palette |
| Title inside figure | Put title in caption |
| Caption requires main text | Make caption self-contained |
| Caption above figure or below table | IEEE: below figure, above table |

### Citation Mistakes

| Mistake | Solution |
|---------|----------|
| Paper-by-paper Related Work | Organize methodologically by approach (inside the single Background and Related Work section) |
| Missing relevant citations | Reviewers may have authored them — cite generously |
| AI-generated citations | Always verify via Xplore / DBLP / CrossRef |
| Inconsistent citation format | Use a single source per entry; clean `refs.bib` |
| `\citet`/`\citep` | Use plain `\cite{}` with the `cite` package |

---

## Pre-Submission Checklist

Before submitting, verify:

**Narrative**:

- [ ] Can state contribution in one sentence
- [ ] Three pillars (What / Why / So What) clear in the introduction
- [ ] Every experiment supports a specific claim

**Structure**:

- [ ] Abstract follows the 5-sentence formula
- [ ] Introduction within budget for the venue (TCAD: 1.5–2 pages; ESL: ~½ page)
- [ ] Methods start by page 3–4 in IEEEtran two-column for a 14-page TCAD paper
- [ ] 2-4 contribution bullets included
- [ ] Overall page allocation matches the budget in [Length Budget](#length-budget-for-ieee-transactions-papers)

**Writing**:

- [ ] Consistent terminology throughout
- [ ] No generic opening sentences
- [ ] Hedging removed unless genuinely necessary
- [ ] All figures have self-contained captions
- [ ] Sentence lengths under 30 words on average

**Technical**:

- [ ] All citations verified via Xplore / DBLP / CrossRef (no hallucinations)
- [ ] Error bars / variance reported where applicable
- [ ] Configurations / tools / settings stated to enable reproducibility
- [ ] Code/data availability stated (if planned)

**IEEE-specific**:

- [ ] `\documentclass[journal,letterpaper]{IEEEtran}`
- [ ] `\bibliographystyle{IEEEtran}` and `\cite{}` everywhere
- [ ] `cite` package loaded (collapses ranges)
- [ ] Captions: below figures, above tables
- [ ] Vector figures only
- [ ] Page count within the venue's target (see `tcad-submission-guide.md`)
