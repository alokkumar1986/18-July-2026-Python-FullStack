import numpy as np
import pandas as pd

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

print(arr)

s = pd.Series(arr, index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

print(s['h'])
