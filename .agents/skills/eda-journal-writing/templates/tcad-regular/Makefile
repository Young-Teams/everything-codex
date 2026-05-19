## ====================================================================
## Makefile for the TCAD template.
##
## Usage:
##   make            -- compile main.pdf with bibtex (default)
##   make quick      -- single pdflatex pass (no bibtex; for fast iteration)
##   make diff       -- generate latexdiff main-diff.pdf vs main-prev.tex
##   make clean      -- remove build artifacts (keeps PDFs)
##   make distclean  -- remove all build artifacts AND the output PDF
## ====================================================================

DOC      := main
LATEX    := pdflatex
BIBTEX   := bibtex
LATEXMK  := latexmk
PREV     := $(DOC)-prev.tex      # set this to the previous-round main.tex
                                 # before running `make diff`

.PHONY: all quick diff clean distclean

all: $(DOC).pdf

$(DOC).pdf: $(DOC).tex refs.bib content/*.tex
	@command -v $(LATEXMK) >/dev/null 2>&1 && \
	    $(LATEXMK) -pdf -interaction=nonstopmode $(DOC).tex || \
	    ($(LATEX) -interaction=nonstopmode $(DOC).tex && \
	     $(BIBTEX) $(DOC) && \
	     $(LATEX) -interaction=nonstopmode $(DOC).tex && \
	     $(LATEX) -interaction=nonstopmode $(DOC).tex)

quick:
	$(LATEX) -interaction=nonstopmode $(DOC).tex

## Generate a diff PDF against the previous-round manuscript.
## Requires `latexdiff` to be installed and $(PREV) to exist.
diff:
	@if [ ! -f $(PREV) ]; then \
	    echo "ERROR: $(PREV) not found. Copy your previous-round main.tex to $(PREV) first."; \
	    exit 1; \
	fi
	latexdiff --flatten $(PREV) $(DOC).tex > $(DOC)-diff.tex
	$(LATEXMK) -pdf -interaction=nonstopmode $(DOC)-diff.tex || true
	@echo "Generated $(DOC)-diff.pdf"

clean:
	rm -f *.aux *.bbl *.blg *.log *.out *.toc *.lof *.lot \
	      *.fls *.fdb_latexmk *.synctex.gz *.nav *.snm *.vrb \
	      content/*.aux

distclean: clean
	rm -f $(DOC).pdf $(DOC)-diff.tex $(DOC)-diff.pdf
