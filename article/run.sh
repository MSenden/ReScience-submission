pandoc --standalone --filter pandoc-fignos --filter pandoc-tablenos --filter pandoc-eqnos --template=rescience-template.tex --latex-engine=xelatex --biblatex --bibliography=senden-schuecker-hahne-diesmann-goebel-2017.bib -M "crossrefYaml=crossref.yaml" --output senden-schuecker-hahne-diesmann-goebel-2017.tex senden-schuecker-hahne-diesmann-goebel-2017.md

xelatex senden-schuecker-hahne-diesmann-goebel-2017
biber senden-schuecker-hahne-diesmann-goebel-2017
xelatex senden-schuecker-hahne-diesmann-goebel-2017
xelatex senden-schuecker-hahne-diesmann-goebel-2017
