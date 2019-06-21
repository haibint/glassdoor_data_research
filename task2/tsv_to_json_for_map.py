import pandas as pd

df = pd.read_csv("semi_final.tsv", sep="\t")


# print(df.groupby('year').count())
# check frequences of years


df_2016 = df.loc[(df['year'] == 2015) & (df["county_code"] != "county_code not found")]
df_2016_simplified = df_2016[["county_code", "city", "net_sentiments_ave"]]
df_renamed = df_2016_simplified.rename(index=str, columns={"county_code": "code", "city": "name", "net_sentiments_ave": "value"})
# df_2016_simplified['net_sentiments_ave'].describe()

# print(df_rename.head)
# [2015, 2016, 2018, 2010, 2012, 2014, 2017, 2008, 2009, 2011, 2013, 2019]
df_renamed.to_json("testing_map_data2.json", orient='records')