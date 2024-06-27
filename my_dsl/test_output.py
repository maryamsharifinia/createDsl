import pandas as pd
inp5 = pd.read_csv("input.csv")

inp5 = inp5.rename(columns={"prodYear": "prod"})

inp5["prod"] = inp5["prod"].astype(float)

inp5 = inp5.sort_values(by="price")

inp5 = inp5.drop(columns=["name"])

inp5["date"] = pd.to_datetime(inp5["date"], errors="coerce")
report = inp5.groupby(inp5["date"].dt.to_period("Y")).size()
print(report)

inp5.to_csv("output.csv", index=False)

import os
os.rename("output.csv", "final_output.csv")
