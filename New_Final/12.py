# Program 12: Avg, highest, lowest using NumPy & Pandas

import numpy as np
import pandas as pd

marks = [78, 92, 67, 85, 90]

arr = np.array(marks)
df = pd.Series(arr)

print("Average:", arr.mean())
print("Highest:", arr.max())
print("Lowest:", arr.min())
