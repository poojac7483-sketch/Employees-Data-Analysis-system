import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../Data/employees.csv")

df["joining_date"] = pd.to_datetime(df["joining_date"])
df["year"] = df["joining_date"].dt.year

joined = df["year"].value_counts().sort_index()

plt.figure(figsize=(8,5))
plt.plot(joined.index, joined.values, marker="o")
plt.title("Employees Joined per Year")
plt.xlabel("Year")
plt.ylabel("Number of Employees")
plt.grid(True)
plt.show()
