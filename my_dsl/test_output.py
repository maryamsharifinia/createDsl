import pandas as pd
inp1 = pd.read_csv("input.csv")

inpNew1 = inp1.rename(columns={"No.": "index", "prodYear": "prod", })

addcol = inp1.copy()
addcol['addCol0'] = inp1["sales"] + inp1["prodYear"]

inp1['addCol1'] = inp1["sales"] + inp1["prodYear"]

addcolnamed = inp1.copy()
addcolnamed["all"] = inp1["sales"] + inp1["prodYear"]

inpdatatype = inpNew1.copy()
inpdatatype[["sales", "prod"]].astype(float)
inp1 = inp1.sort_values(by=["price"])

inp1.drop(columns=["name"])

inp1["date"] = pd.to_datetime(inp1["date"], errors="coerce")
report = inp1.groupby(inp1["date"].dt.to_period("Y")).size()
print(report)

grouped = inp1.groupby(["brand", "price"]).size().reset_index(name="counts")

reorder = inp1[["No.", "brand", "price", "sales", "prodYear", "date", "No.", "price", "brand", "sales", "prodYear", "date"]]

filtered = inp1[inp1["price"]>=100]

searched = inp1[inp1["brand"].str.contains("bm", case=False, na=False)]

inp1["brand"] = inp1["brand"].replace("Benz", "Mercedes")
replaced=inp1
removed = inp1.drop_duplicates(subset=["sales"])

import os
output_directory = os.path.join(os.getcwd(), 'split_data')
if not os.path.exists(output_directory):
    os.makedirs(output_directory)
temp_var = inp1.groupby("region")
for group_name, group_df in temp_var:
    output_file_path = os.path.join(output_directory, f'{group_name}.csv')
    group_df.to_csv(output_file_path, index=False)

combined=inp1
combined["combined_column"] = inp1[["name", "brand", "region", "date"]].apply(lambda row: " ".join(row.values.astype(str)), axis=1)

combined.to_csv("combined.csv", index=False)

removed.to_csv("removed.csv", index=False)

replaced.to_csv("replaced.csv", index=False)

searched.to_csv("searched.csv", index=False)

filtered.to_csv("filtered.csv", index=False)

inp1.to_csv("output.csv", index=False)

reorder.to_csv("reorder.csv", index=False)

grouped.to_csv("grouped.csv", index=False)

addcolnamed.to_csv("add_col_named.csv", index=False)

addcol.to_csv("add_col.csv", index=False)

inpdatatype.to_csv("data_type.csv", index=False)
