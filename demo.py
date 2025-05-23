import pandas as pd
import os

data = {
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35],
    "city": ["New York", "Los Angeles", "Chicago"]
}

df = pd.DataFrame(data)

new_loc = {"name": "madan", "age": "23", "city": "downtown"}

df.loc[len(df.index)] = new_loc

new_loc1 = {"name": "mohon", "age": "25", "city": "los angeles"}

df.loc[len(df.index)] = new_loc1

data_dir = "data"
os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir, "data.csv")

df.to_csv(file_path, index=False)

print(f"Data saved to {file_path}")