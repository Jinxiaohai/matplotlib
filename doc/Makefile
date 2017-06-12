EXE=matplotlib.pdf
SRC=matplotlib.tex
BIB=matplotlib.aux

$(EXE):$(SRC)      ;    xelatex $(SRC)

.PHONY.:look
look:              ;    evince matplotlib.pdf

.PHONY.:clean
clean:             ;    $(RM) matplotlib.aux matplotlib.log matplotlib.pdf matplotlib.dvi matplotlib.bbl matplotlib.blg matplotlib.toc matplotlib.out matplotlib.nav matplotlib.snm matplotlib.thm matplotlib.lot matplotlib.lof
