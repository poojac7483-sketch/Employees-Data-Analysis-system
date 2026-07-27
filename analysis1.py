import pandas as pd
import numpy as np

# Load the data
df = pd.read_csv("../Data/employees.csv")

# Extract the salary column (adjust casing if needed, e.g., df["Salary"])
salary = df["salary"]

# Statistical calculations
print("Mean Salary:", np.mean(salary))
print("Median Salary:", np.median(salary))
print("Variance:", np.var(salary))
print("Standard Deviation:", np.std(salary))
print("Maximum Salary:", np.max(salary))
print("Minimum Salary:", np.min(salary))