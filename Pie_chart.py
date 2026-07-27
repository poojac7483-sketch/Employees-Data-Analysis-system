import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../Data/employees.csv")

avg_salary = df.groupby("department")["salary"].mean()

dept_count = df["department"].value_counts()

plt.figure(figsize=(6,6))
plt.pie(dept_count.values, labels=dept_count.index, autopct="%1.1f%%")
plt.title("Employee Distribution by Department")
plt.show()
