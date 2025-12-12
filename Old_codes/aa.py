import matplotlib.pyplot as plt

departments = ['HR', 'IT', 'Sales', 'Finance']
count = [10, 25, 15, 12]

plt.bar(departments, count, color='lightblue')
plt.title("Employees in Departments")
plt.xlabel("Department")
plt.ylabel("Number of Employees")
plt.show()
