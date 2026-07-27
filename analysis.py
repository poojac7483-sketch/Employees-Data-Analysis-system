import pandas as pd
df = pd.read_csv("../Data/employees.csv")
print(df)

print("Total Employee:", len(df))
print("Highest Salary:", df["salary"].max())
print("Lowest Salary:", df["salary"].min())
print("Average Salary:", df["salary"].mean())
print(df.nlargest(5, "salary"))
print(df.groupby("department")["salary"].mean())
print(df["gender"].value_counts())
print(df["city"].value_counts())
print(df[df["experience"] > 5])
