import numpy as np

mat = np.random.randint(1, 10, (4, 4))
print(mat)
print("Row sums:", np.sum(mat, axis=1))
print("Column sums:", np.sum(mat, axis=0))
