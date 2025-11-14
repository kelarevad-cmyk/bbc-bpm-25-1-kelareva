import pandas as pd

with open('tested.csv') as f:
    titanic = pd.read_csv(f, index_col=0)

print('колво пропусков всего:', titanic.isnull().sum().sum())   # колво пропусков, они есть!!!!!!

print('\nпризнаки и их характер:')      # признаки и их тип
print(titanic.info())

print('\nпервые 5 строк файла:\n', titanic.head())  # первые n строк файла

print('\nбазовая статистика по столбцу Age:\n', titanic['Age'].describe())  #базовая статистика

print('\nколво строк в общем:', titanic.shape[0], 
      '\nколво столбоц:', titanic.shape[1])         # колво строк и заголовков

titanic['Age'] = titanic['Age'].fillna(round(titanic['Age'].agg('mean'), 2))

titanic = titanic['Embarked'].dropna()