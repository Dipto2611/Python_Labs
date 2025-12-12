#add 2 array using numpy and show the null div in try except part

import numpy as np

ar1 = np.array([1, 5, 7, 6])
ar2 = np.array([4, 0, 2, 7])

# Array ops
print("Addition:", ar1 + ar2)
print("Subtraction:", ar1- ar2)
print("Multiply:", ar1 * ar2)

# Division using NumPy
try:
    result = np.divide(ar1, ar2)
    print("Division:", result)

except ZeroDivisionError:
    print("Division by zero occurred")
