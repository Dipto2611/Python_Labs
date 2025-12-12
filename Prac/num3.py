#generate 4*4 matrixx using random

import numpy as np

mat=np.random.randint(1,10,(4,4))
print(mat)
print("Sum of rows:",np.sum(mat,axis=1))
print("Sum of columns:",np.sum(mat,axis=0))

# note: rows for 1, and col for 0