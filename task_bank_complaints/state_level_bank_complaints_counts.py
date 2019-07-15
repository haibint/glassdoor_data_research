import pandas as pd
import json

df = pd.read_stata('data/Consumer_Complaints_Full_ver13.dta', columns=['state'])

# print(df.head)
complaints_counts_dict = {}

for index, row in df.iterrows():
    if complaints_counts_dict.get("US-"+row["state"]) == None:
        complaints_counts_dict["US-"+row["state"]] = 1
    elif complaints_counts_dict.get("US-"+row["state"]) != None:
        complaints_counts_dict["US-"+row["state"]] += 1
    # if index > 100:
    #     print(complaints_counts_dict)
    #     sum = 0
    #     for x in complaints_counts_dict.values():
    #         sum += x
    #     print(sum)
        # break

data_to_write = json.dumps(complaints_counts_dict)

with open('bank_complaints_number_by_state.json', 'w') as outfile:
    outfile.write(data_to_write)
    