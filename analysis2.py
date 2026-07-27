import pandas as pd
import matplotlib.pyplot as plt

# Read CSV
df = pd.read_csv("../Data/employees.csv")

# -------- Bar Chart --------
avg_salary = df.groupby("department")["salary"].mean()

plt.figure(figsize=(8,5))
plt.bar(avg_salary.index, avg_salary.values)
plt.title("Department vs Average Salary")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.show()

# -------- Pie Chart --------
dept_count = df["department"].value_counts()

plt.figure(figsize=(6,6))
plt.pie(dept_count.values, labels=dept_count.index, autopct="%1.1f%%")
plt.title("Employee Distribution by Department")
plt.show()

# -------- Histogram --------
plt.figure(figsize=(8,5))
plt.hist(df["salary"], bins=5)
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")
plt.show()

# -------- Line Chart --------
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