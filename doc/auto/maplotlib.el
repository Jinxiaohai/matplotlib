(TeX-add-style-hook
 "maplotlib"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("ctexbook" "11pt" "UTF8" "hyperref" "openany")))
   (TeX-run-style-hooks
    "latex2e"
    "ctexbook"
    "ctexbook11"
    "amsmath"
    "amssymb"
    "array"
    "booktabs"
    "calc"
    "caption"
    "ctexcap"
    "color"
    "fancyhdr"
    "graphicx"
    "geometry"
    "hyperref"
    "ifthen"
    "longtable"
    "lineno"
    "listings"
    "multicol"
    "makeidx"
    "ntheorem"
    "paralist"
    "tabularx"
    "titlesec"
    "fancyvrb"
    "fontspec"
    "titletoc"
    "xcolor"
    "xeCJK")
   (TeX-add-symbols
    '("mycmdC" 2)
    '("mycmdB" 1)
    "mycmdA")
   (LaTeX-add-index-entries
    "man!haoren"
    "woman!huairen")))

