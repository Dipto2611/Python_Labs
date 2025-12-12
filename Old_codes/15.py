"""Write a Python program to create a dictionary of employees and their
departments. Display only employees belonging to the ‘IT’ department."""

employees = {
    'Arjun': 'HR',
    'Dipto': 'IT',
    'Nayan': 'Finance',
    'Chaya': 'IT'
}

for name, dept in employees.items():
    if dept == 'IT':
        print(name)
