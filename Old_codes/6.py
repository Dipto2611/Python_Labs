'''
Write a Python program to draw a bar chart showing the number of employees
in different departments. Use appropriate labels and title.'''

import matplotlib.pyplot as plt

departments = ['HR', 'IT', 'Sales', 'Finance']
employees = [10, 25, 15, 12]

plt.bar(departments, employees, color='skyblue')
plt.title('Employees in Departments')
plt.xlabel('Department')
plt.ylabel('Number of Employees')
plt.show()
