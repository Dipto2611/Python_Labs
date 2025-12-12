'''Write a Python program using Matplotlib to plot a line chart of monthly sales
for 12 months. Add title and labels to the axes.'''

import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales = [1000, 1200, 900, 1400, 1600, 1300, 1500, 1700, 1550, 1800, 2000, 1900]

plt.plot(months, sales, marker='o', color='green')
plt.title('Monthly Sales Report')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.grid(True)
plt.show()
