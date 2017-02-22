#pandoc --standalone --filter ~/.cabal/bin/pandoc-crossref --template=rescience-template.tex --latex-engine=xelatex --biblatex --bibliography=senden-schuecker-hahne-diesmann-goebel-2017.bib -M "crossrefYaml=crossref.yaml" --output senden-schuecker-hahne-diesmann-goebel-2017.tex senden-schuecker-hahne-diesmann-goebel-2017.md

pandoc --standalone --template=rescience-template.tex --latex-engine=xelatex --biblatex --bibliography=senden-schuecker-hahne-diesmann-goebel-2017.bib -M "crossrefYaml=crossref.yaml" --output senden-schuecker-hahne-diesmann-goebel-2017.tex senden-schuecker-hahne-diesmann-goebel-2017.md

xelatex senden-schuecker-hahne-diesmann-goebel-2017
biber senden-schuecker-hahne-diesmann-goebel-2017
xelatex senden-schuecker-hahne-diesmann-goebel-2017
xelatex senden-schuecker-hahne-diesmann-goebel-2017
