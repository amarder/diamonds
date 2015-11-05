import json
import pandas as pd
import re
import requests


def download(params):
    # Get the data from Blue Nile.
    # http://stackoverflow.com/questions/26165656/rcurl-r-package-geturl-webpage-error-when-scraping-api
    landing_page = requests.get('http://www.bluenile.com/')
    url = 'http://www.bluenile.com/api/public/diamond-search-grid/solr'
    response = requests.get(url, params, cookies=landing_page.cookies)

    # Put the data into a data frame.
    d = json.loads(response.text)
    df = pd.DataFrame(d['results'])

    # Clean up the data.
    for col in ['carat', 'depth', 'lxwRatio', 'table']:
        df[col] = df[col].astype(float)
    for col in ['price', 'pricePerCarat']:
        df[col] = df[col].map(lambda s: re.sub('[$,]', '', s)).astype(int)

    return df


shapes = [
        "AS", # asscher
        "CU", # cushion
        "EC", # emerald
        "HS", # heart
        "MQ", # marquise
        "OV", # oval
        "PR", # princess
        "PS", # pear
        "RA", # radiant
        "RD", # round
    ]
cuts = ['Good', 'Very Good', 'Ideal', 'Signature Ideal']
colors = ['J', 'I', 'H', 'G', 'F', 'E', 'D']
clarities = ['SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF', 'FL']
options = {
    'shape': shapes,
    'minPrice': int,
    'maxPrice': int,
    'minCarat': float,
    'maxCarat': float, 
    'minCut': cuts,
    'maxCut': cuts,
    'minColor': colors,
    'maxColor': colors,
    'minClarity': clarities,
    'maxClarity': clarities,
    'startIndex': int,
    'pageSize': int,
}


if __name__ == '__main__':
    params = {
        'country': 'USA',
        'language': 'en-us',
        'currency': 'USD',
        'startIndex': 0,
        'pageSize': 10,
        'shape': ['RD', 'CU'],
    }

    df = download(params)
    print df
    print df.dtypes
