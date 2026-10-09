# name   'Aptech'
# age    10   
# course  'Python'
# address 'Bangalore'
# marks  90

import numpy as np
import pandas as pd

calories = { 'name': 'Aptech', 'age': 10, 'course': 'Python', 'address': 'Bangalore', 'marks': 90}
s = pd.Series(calories)

print(s)
