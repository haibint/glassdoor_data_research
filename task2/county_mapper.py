import pandas as pd

df_stata = pd.read_stata('../stata_files/sum_city_year.dta')
df_matched_counties = pd.read_csv('matched_counties_with_code.tsv', sep="\t")


# year_list = []

def year_range_checker(year):
    if year not in year_list:
        year_list.append(year)


state_matching_row_count = 0
output_dataframe = pd.DataFrame()
# print(df_stata.loc[df_stata['city'] == "Cherokee"])
print(len(df_stata))

for index, row in df_matched_counties.iterrows():
    county_data_by_year = df_stata.loc[df_stata['city'] == row['county']]
    # then filer the rows with state name to make sure the counties in questions are in the same state
    filered_county_data_by_year = county_data_by_year.loc[county_data_by_year['state'] == row['full_name'][-2:]]
    
    # for sub_index, sub_row in filered_county_data_by_year.iterrows():
    #     year_range_checker(sub_row['year'])
    # print(county_data_by_year['state'])
    # print('~~~~~~~~~~~~~~~~~')
    # print(row['full_name'][-2:])
    # print('----------------')
    # print(filered_county_data_by_year)
    if len(filered_county_data_by_year) > 0:
        filered_county_data_by_year["county_code"] = row['county_code']
        # print(filered_county_data_by_year)
        if len(output_dataframe) == 0:
            output_dataframe = filered_county_data_by_year
            state_matching_row_count = state_matching_row_count +1
            # drop the df_stata for those get matched.
            continue
        output_dataframe = pd.concat([output_dataframe, filered_county_data_by_year], ignore_index=True)
        state_matching_row_count = state_matching_row_count +1

    if state_matching_row_count%50 < 1:
        print(state_matching_row_count)
        



# checking how many rows or matched counties previously are actually in the same state. answer: 624
# print(state_matching_row_count)
print(len(output_dataframe))
output_dataframe.to_csv("map_data.tsv", sep="\t"， encoding='utf-8')
# checking year range. [2015, 2016, 2018, 2010, 2012, 2014, 2017, 2008, 2009, 2011, 2013, 2019]
# print(year_list)