'''Write a Python program to input names and salaries of employees, store them
in lists, and display the name of the employee with the highest salary.'''


n = int(input("Enter number of employees: "))
names, salaries = [], []

for i in range(n):
    names.append(input("Enter name: "))
    salaries.append(float(input("Enter salary: ")))

index = salaries.index(max(salaries))
print("Highest salary is of:", names[index], "→", salaries[index])
