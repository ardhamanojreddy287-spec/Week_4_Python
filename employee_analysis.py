import pandas as pd

# Load employee data
df = pd.read_csv("employees.csv")

print("===== EMPLOYEE DATA =====")
print(df)

# Average salary
average_salary = df["Salary"].mean()

print("\n===== AVERAGE SALARY =====")
print(f"Average Salary: ₹{average_salary:.2f}")

# Department count
department_count = df["Department"].value_counts()

print("\n===== EMPLOYEES BY DEPARTMENT =====")
print(department_count)

# Salary threshold
salary_threshold = 50000

high_salary = df[df["Salary"] > salary_threshold]

print(f"\n===== EMPLOYEES WITH SALARY ABOVE ₹{salary_threshold} =====")
print(high_salary)

# Export filtered employees
high_salary.to_csv("high_salary_employees.csv", index=False)

print("\nFiltered employee data exported successfully!")
print("File created: high_salary_employees.csv")