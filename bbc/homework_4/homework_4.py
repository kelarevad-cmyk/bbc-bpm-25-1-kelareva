import pandas as pd
import numpy as np
with open('tested.csv') as f:
    titanic = pd.read_csv(f)

print('колво пропусков всего:', titanic.isnull().sum().sum())   #колво пропусков, они есть!!!!!!

print('\nпризнаки и их характер:')
print(titanic.info())

print('\nпервые 5 строк файла:\n', titanic.head())

titanic['Age'] = titanic['Age'].fillna(round(titanic['Age'].agg('mean'), 2))
