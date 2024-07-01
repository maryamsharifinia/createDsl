import pandas as pd
inp5 = pd.read_csv("input.csv")

inp5 = inp5.rename(columns={"prodYear": "prod"})

inp5.to_csv("abcd_out.csv", index=False)
