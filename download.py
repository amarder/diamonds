import json
import pandas as pd
import re
import requests
import argparse
import warnings


def download(params):
    # Get the data from Blue Nile.
    # http://stackoverflow.com/questions/26165656/rcurl-r-package-geturl-webpage-error-when-scraping-api
    landing_page = requests.get('http://www.bluenile.com/')
    url = 'http://www.bluenile.com/api/public/diamond-search-grid/solr'
    response = requests.get(url, params, cookies=landing_page.cookies)

    # Put the data into a data frame.
    d = json.loads(response.text)
    N = int(d['countRaw'])
    n = len(d['results'])
    if n < N:
        msg = "You've downloaded %d of %d diamonds." % (n, N)
        warnings.warn(msg)
    df = pd.DataFrame(d['results'])

    # Clean up the data.
    for col in ['carat', 'depth', 'lxwRatio', 'table']:
        df[col] = df[col].astype(float)
    for col in ['price', 'pricePerCarat']:
        df[col] = df[col].map(lambda s: re.sub('[$,]', '', s)).astype(int)

    return df


def parse_arguments():
    parser = argparse.ArgumentParser()

    shapes = [
        "RD",  # round
        "PR",  # princess
        "EC",  # emerald
        "AS",  # asscher
        "CU",  # cushion
        "MQ",  # marquise
        "RA",  # radiant
        "OV",  # oval
        "PS",  # pear
        "HS",  # heart
    ]
    parser.add_argument('--shape', nargs='+', choices=shapes)

    parser.add_argument('--minPrice', type=int)
    parser.add_argument('--maxPrice', type=int)
    parser.add_argument('--minCarat', type=float)
    parser.add_argument('--maxCarat', type=float)

    cuts = ['Good', 'Very Good', 'Ideal', 'Signature Ideal']
    colors = ['J', 'I', 'H', 'G', 'F', 'E', 'D']
    clarities = ['SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF', 'FL']
    select_one = [
        ('minCut', cuts),
        ('maxCut', cuts),
        ('minColor', colors),
        ('maxColor', colors),
        ('minClarity', clarities),
        ('maxClarity', clarities),
    ]
    for key, choices in select_one:
        parser.add_argument('--%s' % key, choices=choices)

    arguments_with_defaults = [
        ('startIndex', 0),
        ('pageSize', 10),
        ('country', 'USA'),
        ('language', 'en-us'),
        ('currency', 'USD'),
    ]
    for k, v in arguments_with_defaults:
        parser.add_argument('--%s' % k, default=v, type=type(v))

    args = parser.parse_args()
    d = args.__dict__
    for k, v in d.items():
        if v is None:
            del d[k]
    return d


def main():
    params = parse_arguments()
    df = download(params)
    print df.to_csv(index=False)


if __name__ == '__main__':
    main()
