diamonds.csv: download.py
	python download.py --shape RD --minPrice 1000 --maxPrice 2000 --pageSize 1001 > diamonds.csv

diamonds.md: diamonds.Rmd diamonds.csv
	Rscript -e "knitr::knit('diamonds.Rmd')"
