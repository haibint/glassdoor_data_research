import pandas as pd
import json

df_stata = pd.read_stata('../stata_files/sum_state_year.dta')
# unique years in this dataframe [2008 2009 2010 2011 2012 2013 2014 2015 2016 2017 2018 2019]
# print(df_stata.year.unique())

for year in range(2008, 2020):
    df_year = df_stata.loc[(df_stata['year'] == year)]
    df_year_simplified = df_year[["state", "net_sentiments_ave"]]
    # print(df_year.head)
    data = "{"
    for index, row in df_year_simplified.iterrows():
        data += '"'+ "US-"+ row['state'] +'"' + ":"+ '"'+ "{0:.2f}".format(round(row["net_sentiments_ave"],2)) +'"' + ",\n"
    data = data[:-2] + "}"
    with open(str(year)+'_state_average.json', 'w') as outfile:  
        outfile.write(data)

