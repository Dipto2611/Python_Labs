import matplotlib.pyplot as p

x = [1, 2, 3, 4, 5]
y1 = [10, 8, 6, 14, 7]
y2 = [4, 2, 8, 6, 5]

p.bar(x, y1, width=0.4, label="Y1")
p.bar(x, y2, width=0.4, bottom=y1, label="Y2")   # stacked on top

p.title("Stacked Bar Graph")
p.legend()
p.show()


#################################################################
import matplotlib.pyplot as p
import numpy as np

x = np.array([1, 2, 3, 4, 5])

y1 = [10, 8, 6, 14, 7]
y2 = [4, 2, 8, 6, 5]

width = 0.3   # bar width

p.bar(x - width/2, y1, width, label="Y1")
p.bar(x + width/2, y2, width, label="Y2")

p.title("Double Bar Graph")
p.legend()
p.show()
