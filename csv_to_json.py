import pandas as pd

df = pd.read_csv("data/customers.csv")

# Export file content to json
df.to_json("data/customers.json", orient="records", lines=False)
