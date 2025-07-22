TEXFILES=$(wildcard *.tex)
PDFS=$(TEXFILES:.tex=.pdf)

all: $(PDFS)

%.pdf: %.tex
	lualatex -interaction=nonstopmode $<

clean:
$(RM) $(PDFS) *.log *.aux *.toc *.out

.PHONY: all clean
