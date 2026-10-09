import numpy as np
import pandas as pd

calories = { 'day1': 420, 'day2': 380, 'day3': 390, 'day4': 410, 'day5': 400 }
s = pd.Series(calories, index=['day3','day5'])

print(s)