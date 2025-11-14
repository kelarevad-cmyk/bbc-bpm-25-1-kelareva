import pandas as pd
import numpy as np
with open('tested.csv') as f:
    titanic = pd.read_csv(f)
print(titanic.isnull().sum())