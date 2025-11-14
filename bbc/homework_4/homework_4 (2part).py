import pandas as pd
import numpy as np
#columns: PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
with open('tested.csv') as f:
    titanic = pd.read_csv(f, index_col=0)

survive_count = len(titanic['Survived'])

survived_male = titanic['Survived'].loc[titanic['Sex'] == 'male'].sum() / survive_count
survived_female = titanic['Survived'].loc[titanic['Sex'] == 'female'].sum() / survive_count

print(f'процент выживыших м = {survived_male * 100:.2f}%, процент выживших ж = {survived_female * 100:.2f}%')


filter1 = titanic.loc[(titanic['Age'] > 30)
                      & (titanic['Sex'] == 'male')
                     & (titanic['Pclass'])]

filter2 = titanic.loc[((titanic['Age'] < 18)
                      | (titanic['Sex'] == 'female'))
                      & (titanic['Survived'])]

new_titanic = titanic.groupby(['Pclass', 'Sex'])
print(new_titanic['Age'].agg('mean'))
print(new_titanic['Survived'].apply(lambda x: (x.sum() / x.count()) * 100))
print(new_titanic['Fare'].agg('mean'))
