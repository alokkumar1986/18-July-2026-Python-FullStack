import numpy as np

x = np.arange(8)  

y = x.reshape(2, 4)

z = x.reshape(2, 4, 1)

print(x)

print(x.shape)
print(y)
print(y.shape)
print(z)
print(z.shape)