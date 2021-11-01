import pandas as pd
from tqdm.cli import tqdm
import os, re, sys
from KeywordFetcher import *
from TrendSetter import *

filename = str(sys.argv[1])
# filename = str('1.csv')
keywords = get_keywords(filename)

trend_df = []
for geo_location in keywords.geo_location.unique().tolist():
    if os.path.isdir(os.path.join('MetaTrend', geo_location)):
        for file in tqdm(os.listdir(os.path.join('MetaTrend', geo_location))):
            iot_df = pd.read_csv(os.path.join('MetaTrend', geo_location, file))
            iot_df.drop(['isPartial'], axis = 1, inplace=True)
            iot_df = iot_df.set_index('date').sort_index()
            trend_df.append(iot_df)
        trend_df = pd.concat(trend_df, axis=1)
        df = raw_cleaner(trend_df, filename)
# print(trend_df.tail())
