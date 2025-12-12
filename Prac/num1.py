#high low marks of the std using numpy

import numpy as np

ar=np.array([[12,45,78,85,44],[48,65,71,20,13]]) #its 2d array
print(ar)
print("its the eg for 2d arr")

#############################################################
# from here check the code and the upper section is for understanding:

newm=np.array([12,45,78,85,44]) #main eg:
print()
print("avg:",np.average(newm))
print("min marks:",np.min(newm))
print("max marks:",np.max(newm))
print("std :",np.std(newm))



# print("max marks:",np.maximum(newm)) not possible 