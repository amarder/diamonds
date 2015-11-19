rounds.csv: download.py
	python download.py --shape RD > rounds.csv

diamonds.html: diamonds.Rmd rounds.csv
	Rscript -e "knitr::knit2html('diamonds.Rmd')"

BLOG = ~/Dropbox/amarder.github.io
IMG_FOLDER = $(BLOG)/static/images/diamonds
IMG_URL = /images/diamonds

blog: diamonds.html
	rm -r $(IMG_FOLDER)
	cp -r figure $(IMG_FOLDER)
	sed "s+(figure/+($(IMG_URL)/+" diamonds.md > $(BLOG)/content/post/diamonds.md
