import pandas as pd
import numpy as np

with open('tested.csv') as f:
    titanic = pd.read_csv(f, index_col=0)
