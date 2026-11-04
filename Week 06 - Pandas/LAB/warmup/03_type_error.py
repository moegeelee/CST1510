# Convert numeric text to integers before dividing the columns.

import pandas as pd

df = pd.DataFrame({"value": ["87", "120", "45"], "limit": [100, 100, 100]})

df["value"] = df["value"].astype(int)
df["percent"] = (df["value"] / df["limit"]) * 100
print(df)
