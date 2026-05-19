# IEEE-Style Citation Workflow (TCAD / TVLSI)

This document describes the **programmatic, hallucination-proof** citation workflow for EDA journal papers. It is the IEEE-style counterpart of the ml-paper-writing skill's citation workflow.

> **🚨 Golden Rule:** NEVER write BibTeX entries from memory. ALWAYS fetch them from a verifiable source. AI-generated citations have a ~40% error rate, and TCAD editors routinely catch fabricated references.

---

## 1. The Recommended Search Order

For EDA papers, the optimal search order — from highest to lowest precision — is:

| Rank | Source | Best for | Quality |
|------|--------|----------|---------|
| 1 | **IEEE Xplore** | IEEE conferences & journals (DAC, ICCAD, DATE, ISCAS, TCAD, TVLSI, ASP-DAC, ISLPED) | Authoritative BibTeX |
| 2 | **ACM Digital Library** | ACM venues (DAC in ACM years, ISPD, GLSVLSI, FPGA) | Authoritative |
| 3 | **DBLP** | Fast cross-venue search for any EDA author | Compact, clean BibTeX |
| 4 | **CrossRef (DOI lookup)** | Anything with a DOI | Universal |
| 5 | **Semantic Scholar API** | Cross-source metadata + paperId-based linkages | Good for novelty checks |
| 6 | **arXiv** | Preprints (mostly ML-for-EDA papers) | Preprints only |
| 7 | **Google Scholar** | Last-resort search; manual export | Imprecise BibTeX |

> Most EDA papers live on **IEEE Xplore**, so it is the primary source.

---

## 2. The Per-Citation Workflow

```
For every citation, follow these steps in order:

[ ] Step 1: Search the title in DBLP or IEEE Xplore
[ ] Step 2: Verify the paper exists in ≥ 2 sources (Xplore + DBLP, or DOI + arXiv)
[ ] Step 3: Fetch BibTeX from the most authoritative source (Xplore preferred)
[ ] Step 4: Verify the claim you are citing actually appears in the paper
[ ] Step 5: Paste the verified BibTeX into refs.bib
[ ] Step 6: If ANY step fails → mark as PLACEHOLDER, tell the scientist
```

---

## 3. IEEE Xplore — Manual Workflow

For most TCAD-relevant papers, IEEE Xplore is the source of truth.

1. Open <https://ieeexplore.ieee.org/>.
2. Search by title (best) or title + first author.
3. Open the paper's landing page.
4. Click **"Cite This"** → choose **"BibTeX"** → **"Download"**.
5. Open the downloaded `.bib` file and paste into your `refs.bib`.
6. Optionally clean: remove `keywords = {...}` field if you want minimal entries.

Example IEEE Xplore BibTeX:

```bibtex
@ARTICLE{liu2024deeplearning,
  author={Liu, Yibo and Pan, David Z.},
  journal={IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems},
  title={Deep Learning for Standard-Cell Placement: A Survey},
  year={2024},
  volume={43},
  number={9},
  pages={2891-2918},
  doi={10.1109/TCAD.2024.XXXXXXX}
}
```

> **Tip:** IEEE Xplore's `journal={...}` field uses the full journal name. Some IEEEtran configurations prefer the abbreviated form (e.g., `IEEE Trans. Comput.-Aided Des. Integr. Circuits Syst.`). Both are accepted, but stay consistent throughout `refs.bib`.

---

## 4. DBLP — Fast Programmatic Search

DBLP is the fastest way to look up EDA authors and venues.

### Manual

1. Open <https://dblp.org/>.
2. Search by author or title.
3. On the result, click the small **`[BIB]`** or **`bibtex`** icon (or paper detail → "Export record").
4. Choose **"BibTeX (condensed)"** for short entries or **"BibTeX (standard)"** for full.

### Programmatic (Python)

```python
import requests

def dblp_search(query: str, max_results: int = 5):
    """Search DBLP and return a list of papers."""
    url = "https://dblp.org/search/publ/api"
    params = {"q": query, "format": "json", "h": max_results}
    r = requests.get(url, params=params, timeout=15)
    r.raise_for_status()
    hits = r.json()["result"]["hits"].get("hit", [])
    return [h["info"] for h in hits]

def dblp_bibtex_by_key(dblp_key: str) -> str:
    """Fetch BibTeX from a DBLP key, e.g., 'journals/tcad/SmithJ24'."""
    url = f"https://dblp.org/rec/{dblp_key}.bib?param=1"  # standard format
    r = requests.get(url, timeout=15)
    r.raise_for_status()
    return r.text

# Example
results = dblp_search("placement legalization ILP TCAD", max_results=3)
for p in results:
    print(p.get("title"), "—", p.get("venue"), p.get("year"))
    key = p["key"]
    print(dblp_bibtex_by_key(key))
```

---

## 5. CrossRef DOI → BibTeX

For any paper with a DOI, CrossRef returns canonical BibTeX:

```python
import requests

def doi_to_bibtex(doi: str) -> str:
    """Get verified BibTeX from DOI via CrossRef."""
    r = requests.get(
        f"https://doi.org/{doi}",
        headers={"Accept": "application/x-bibtex"},
        timeout=15,
    )
    r.raise_for_status()
    return r.text

print(doi_to_bibtex("10.1109/TCAD.2022.3186742"))
```

---

## 6. Semantic Scholar — Cross-Source Search

Use Semantic Scholar to (a) find a paper when you only know the rough topic and (b) confirm that a paper exists in more than one database.

```python
from semanticscholar import SemanticScholar

sch = SemanticScholar()
results = sch.search_paper(
    "placement legalization mixed-size ePlace",
    limit=5,
    fields=["title", "year", "externalIds", "venue", "authors"],
)
for paper in results:
    title = paper.title
    year = paper.year
    venue = paper.venue
    doi = (paper.externalIds or {}).get("DOI")
    print(f"{title} ({venue}, {year}) — DOI: {doi}")
```

Then call `doi_to_bibtex(doi)` to get the BibTeX, or fall back to DBLP / Xplore if DOI is missing.

---

## 7. arXiv Lookup

For ML-for-EDA papers that exist only as preprints:

```python
import urllib.parse
import xml.etree.ElementTree as ET
import requests

def arxiv_search(query: str, max_results: int = 5):
    base = "http://export.arxiv.org/api/query"
    q = urllib.parse.urlencode({
        "search_query": f"ti:{query}",
        "max_results": max_results,
    })
    r = requests.get(f"{base}?{q}", timeout=15)
    r.raise_for_status()
    root = ET.fromstring(r.text)
    ns = {"a": "http://www.w3.org/2005/Atom"}
    for entry in root.findall("a:entry", ns):
        title = entry.find("a:title", ns).text.strip()
        link = entry.find("a:id", ns).text  # https://arxiv.org/abs/XXXX.YYYYY
        print(title, "—", link)
```

arXiv preprints can be cited via:

```bibtex
@misc{author2024shorttitle,
  title={Full Title},
  author={Author, F. and Coauthor, S.},
  year={2024},
  eprint={2401.12345},
  archivePrefix={arXiv},
  primaryClass={cs.AR}
}
```

Once an arXiv paper is published at a venue, **switch the citation to the venue version** before submission.

---

## 8. Verifying the Claim

Once you have a verified BibTeX entry, you still need to confirm the **claim** you are citing actually appears in the paper. Common errors:

1. Citing a survey for a specific result it doesn't contain
2. Citing the wrong paper from the same author group
3. Citing a paper that proposes a technique for the technique's *evaluation*, not *origin*
4. Citing a paper whose claim is the opposite of what you imply

A practical check:

```
For each \cite{key}, write down on a scratchpad:
  - The exact claim I'm attributing to this paper
  - Page or section in the paper where this claim appears
  - One-sentence quote from the paper supporting the claim
```

If you cannot complete this exercise for a citation, it should be either rephrased or removed.

---

## 9. Citation Style Conventions (IEEE)

### Use the `cite` package

```latex
\usepackage{cite}
```

This automatically collapses `[1,2,3,4]` → `[1]–[4]` and sorts within brackets.

### Single citation

```latex
prior work \cite{smith2024} has shown that ...
```

### Multiple citations

```latex
several methods \cite{smith2024, jones2023, lee2022} address this problem
```

### Citation as a noun (avoid)

❌ `\cite{smith2024} showed that ...`
✅ `Smith et al. \cite{smith2024} showed that ...`

### Et al. usage

For 3+ authors, use "et al." (in italics: `\textit{et al.}`) at first and subsequent mentions. IEEEtran handles this when you use `\cite{}` properly.

For exactly 2 authors, use both names: "Smith and Jones [12]".

For 1 author, use that name: "Smith [12]".

### Citation positioning

IEEE style places the citation after the relevant claim:

✅ "The proposed method achieves the lowest area among existing approaches [12, 14]."
✅ "The proposed method achieves the lowest area among existing approaches, including ABC [12] and LSOracle [14]."

---

## 10. Common BibTeX Field Conventions for IEEEtran

| Field | Required for | Notes |
|-------|--------------|-------|
| `author` | All entries | Use `and` to join: `Smith, J. and Jones, K.` |
| `title` | All entries | Capitalize properly; wrap proper nouns in `{...}` |
| `year` | All entries | 4-digit year |
| `journal` | `@article` | Full or abbreviated, but consistent |
| `booktitle` | `@inproceedings` | Conference name |
| `pages` | Preferred | `XXX--YYY` (en-dash) |
| `volume`, `number` | Journals | If known |
| `doi` | Preferred | `10.1109/...` |
| `publisher` | `@inproceedings` for ACM | Often unnecessary for IEEEtran |
| `month` | Optional | IEEE style omits month for brevity |

### Capitalization in titles

BibTeX downcases titles by default with IEEEtran-bst. Protect proper nouns:

```bibtex
@article{liu2024,
  title={{ABC}-based optimization for {AIG} networks},
  ...
}
```

Without the braces, "ABC" would render as "Abc" in the bibliography.

---

## 11. Handling Common Citation Cases in EDA

### A. Citing a tool

For tools, prefer the originating paper, not a website. Then optionally add a URL footnote in the text.

```bibtex
@inproceedings{abc,
  author={Mishchenko, Alan and others},
  title={{ABC}: A System for Sequential Synthesis and Verification},
  booktitle={UC Berkeley Tech Note},
  year={2007}
}
```

In text: "We use ABC \cite{abc} (commit \texttt{abc70930}) for technology mapping."

### B. Citing a benchmark suite

```bibtex
@inproceedings{itc99,
  author={Corno, F. and Reorda, M. Sonza and Squillero, G.},
  title={{RT}-Level {ITC'99} Benchmarks and First {ATPG} Results},
  booktitle={Proc. IEEE International Test Conference (ITC)},
  year={1999}
}
```

### C. Citing a PDK

PDKs usually have a manual rather than a paper. Cite the technical report:

```bibtex
@techreport{nangate45,
  title={{NanGate} {FreePDK45} Open Cell Library},
  institution={NanGate Inc.},
  year={2008},
  note={\url{http://www.nangate.com/}}
}
```

### D. Citing a software repository

If you must cite code (e.g., your own DREAMPlace), prefer the paper:

```bibtex
@inproceedings{dreamplace,
  author={Lin, Yibo and others},
  title={{DREAMPlace}: Deep Learning Toolkit-Enabled {GPU} Acceleration for Modern {VLSI} Placement},
  booktitle={Proc. DAC},
  year={2019}
}
```

If no paper exists, use `@misc` with a URL:

```bibtex
@misc{repo,
  title={{ToolName}: A short description},
  author={Author Name},
  year={2024},
  howpublished={\url{https://github.com/org/repo}},
  note={Accessed: 2024-MM-DD}
}
```

---

## 12. End-of-Workflow Checks

Before submission, run these checks on `refs.bib`:

- [ ] No `@misc` entries that should be `@article` or `@inproceedings`
- [ ] All DOIs are valid (test: `curl -I https://doi.org/<DOI>` should redirect)
- [ ] All `title` fields have proper noun protection
- [ ] All authors are listed in `Last, First` form with `and` separator
- [ ] Year and venue match what's reported in the body of the paper
- [ ] No two entries refer to the same paper with different keys
- [ ] No keys named `PLACEHOLDER_*` remain (verify before submission)
- [ ] BibTeX runs without warnings: `bibtex main` produces no missing fields

A simple sanity script:

```bash
# Find any remaining placeholders
grep -n "PLACEHOLDER" main.tex *.bib

# Verify references all resolve
pdflatex main.tex >/dev/null
bibtex   main
pdflatex main.tex >/dev/null
pdflatex main.tex 2>&1 | grep -E "Warning|undefined"
```

---

## 13. When You Genuinely Cannot Find a Citation

If a reviewer mentions a paper by approximate title and you cannot find it:

1. Search the title variants in DBLP and IEEE Xplore.
2. Search the first author's DBLP page directly.
3. Search Google Scholar with quoted exact phrases.
4. If still unfound, write back to the reviewer in the response letter:

> "We were unable to locate the reference suggested by the reviewer. Could the reviewer kindly provide the full citation or a DOI? In the meantime, we have added two related works ([X], [Y]) that we believe cover similar ground."

Reviewers respect this — it is far better than citing a hallucinated paper.

---

## 14. Quick Reference Card

```
Want to cite ...                Use this source first
────────────────────────────────────────────────────
TCAD / TVLSI / TC paper      →  IEEE Xplore
DAC / ICCAD / DATE paper     →  IEEE Xplore
ISPD / GLSVLSI / FPGA paper  →  ACM Digital Library
HLS or arch paper at MICRO   →  ACM DL or IEEE Xplore
arXiv-only preprint          →  arXiv
Survey / book chapter        →  DOI via CrossRef
Open-source tool (no paper)  →  @misc with URL
Benchmark suite              →  Original paper (IEEE Xplore / ACM DL)
PDK                          →  @techreport from vendor docs
Your own conference paper    →  IEEE Xplore / ACM DL; mark in cover letter
```

---

**🚨 Reminder: NEVER write BibTeX from memory. ALWAYS fetch programmatically or from a verifiable source. 🚨**
