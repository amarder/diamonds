# Identifying deals on Blue Nile

1. `download.py` - command line tool to download data (price and characteristics) of diamonds on Blue Nile.

2. `diamonds.Rmd` - R Markdown report that models price as a function of cut, color, clarity, and carat weight. Diamonds with the smallest actual price to expected price are the best deals.

3. `Makefile` - a file to tie it all together. Use `make diamonds.html` at the command line to download data on all round cut diamonds on Blue Nile and compile the report.
