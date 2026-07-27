import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../Data/employees.csv")

avg_salary = df.groupby("department")["salary"].mean()

plt.figure(figsize=(8,5))
plt.bar(avg_salary.index, avg_salary.values)
plt.title("Department vs Average Salary")
plt.xlabel("Department")
plt.ylabel("Average Salary")

# Save the chart
plt.savefig("../Charts/bar_chart.png")

# Display the chart
plt.show()