import numpy as np

x = np.arange(8)  

y = x.reshape(2, 4)

z = y.reshape(2, 4, 1)

print(z)