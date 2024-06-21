import pandas as pd
input_df = pd.read_csv("input.csv")

output_df="output.csv"

df1 = pd.read_csv("file1.csv")
df2 = pd.read_csv("file2.csv")
df_combined = pd.concat([df1, df2])
df_combined.to_csv("output.csv", index=False)

df = pd.read_csv("input.csv")
df.to_excel("output.xls", index=False)

df = pd.read_excel("input.xls")
df.to_csv("output.csv", index=False)

input_df["profit"] = input_df["sales"] + input_df["expenses"]
input_df.to_csv( output_df , index=False)

input_df = input_df.rename(columns={"age": "customer_age"})
input_df.to_csv( output_df , index=False)
