import matplotlib.pyplot as p

# Scatter plot
x = [1, 1.3, 2, 4, 5]
y = [10, 8, 6, 14, 7]

p.subplot(1,2,1)
p.scatter(x, y)
p.xlabel("X axis")
p.ylabel("Y axis")
p.title("Scatter Plot")
p.grid()
# p.show()

# Bar graph
days = ["mon", "tue", "wed", "thu", "fri"]
values = [10, 8, 6, 14, 7]


p.subplot(1,2,2)
p.bar(days, values)    # string labels + numeric heights
p.xlabel("Days")
p.ylabel("Values")
p.title("Bar Graph")

p.tight_layout()

p.show()

