# http://www.bluenile.com/api/public/build-your-own-ring/diamond-search-grid?country=USA&language=en-us&currency=USD&startIndex=0&pageSize=250000&shape=RD

import json
import pandas as pd
import re
from matplotlib import pyplot as plt

with open('diamonds.json') as f:
    d = json.load(f)

df = pd.DataFrame(d['results'])
df['price'] = df.price.map(lambda s: re.sub('[$,]', '', s)).astype(int)
df['carat'] = df.carat.astype(float)

df.to_csv('diamonds.csv')
