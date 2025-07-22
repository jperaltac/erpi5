TEXFILES=$(wildcard *.tex)
PDFS=$(TEXFILES:.tex=.pdf)

all: $(PDFS)

%.pdf: %.tex
	lualatex -interaction=nonstopmode -halt-on-error -shell-escape $<

clean:
	$(RM) $(PDFS) *.log *.aux *.toc *.out

.PHONY: all clean
