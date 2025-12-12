'''Write a Python program using Matplotlib to draw a pie chart showing the
percentage distribution of students in different streams.'''

import matplotlib.pyplot as plt

streams = ['Science', 'Commerce', 'Arts', 'Vocational']
students = [50, 30, 15, 5]

plt.pie(students, labels=streams, autopct='%1.1f%%', startangle=90)
plt.title('Students Distribution by Stream')
plt.show()
