import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../Data/employees.csv")



plt.figure(figsize=(8,5))
plt.hist(df["salary"], bins=5)
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")
plt.show()
