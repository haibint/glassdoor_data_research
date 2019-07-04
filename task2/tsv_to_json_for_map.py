import pandas as pd

df = pd.read_csv("./data/semi_final.tsv", sep="\t")
# [2015, 2016, 2018, 2010, 2012, 2014, 2017, 2008, 2009, 2011, 2013, 2019]

# print(df.groupby('year').count())
# check frequences of years
for year in [2018, 2010, 2012, 2014, 2017, 2008, 2009, 2011, 2013, 2019]:
    df_year = df.loc[(df['year'] == year) & (df["county_code"] != "county_code not found")]
    df_year_simplified = df_year[["county_code", "city", "net_sentiments_ave"]]
    df_renamed = df_year_simplified.rename(index=str, columns={"county_code": "code", "city": "name", "net_sentiments_ave": "value"})
    # df_2016_simplified['net_sentiments_ave'].describe()

    # print(df_rename.head)
    df_renamed.to_json("../web_interface/json/county_level_sentiment_"+ str(year) +".json", orient='records')
