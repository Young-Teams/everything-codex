## ====================================================================
## Makefile for the response-to-reviewers letter.
##
## Usage:
##   make           -- compile response.pdf
##   make clean     -- remove build artifacts (keeps PDF)
##   make distclean -- remove everything generated
## ====================================================================

DOC := response
LATEX := pdflatex
LATEXMK := latexmk

.PHONY: all clean distclean

all: $(DOC).pdf

$(DOC).pdf: $(DOC).tex
	@command -v $(LATEXMK) >/dev/null 2>&1 && \
	    $(LATEXMK) -pdf -interaction=nonstopmode $(DOC).tex || \
	    ($(LATEX) -interaction=nonstopmode $(DOC).tex && \
	     $(LATEX) -interaction=nonstopmode $(DOC).tex)

clean:
	rm -f *.aux *.log *.out *.toc *.fls *.fdb_latexmk *.synctex.gz

distclean: clean
	rm -f $(DOC).pdf
