rounds.csv: download.py
	python download.py --shape RD > rounds.csv

diamonds.html: diamonds.Rmd rounds.csv
	Rscript -e "knitr::knit2html('diamonds.Rmd')"
