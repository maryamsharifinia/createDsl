import pandas as pd
inp1 = pd.read_csv("input.csv")



sheet_id = "1Qdz1B7Ky4y7DYk-F3Z1gIOdL6BMV5DqJwDXSzQazm_o"
local_path = "test1.csv"
csv_export_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv"
df = pd.read_csv(csv_export_url)
df.to_csv(local_path, index=False)

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

inp1.to_csv("output.csv", index=False)

reorder.to_csv("reorder.csv", index=False)

grouped.to_csv("grouped.csv", index=False)

addcolnamed.to_csv("add_col_named.csv", index=False)

addcol.to_csv("add_col.csv", index=False)

inpdatatype.to_csv("data_type.csv", index=False)
