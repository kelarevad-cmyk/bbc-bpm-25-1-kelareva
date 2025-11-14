import pandas as pd
import numpy as np
#columns: PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
with open('tested.csv') as f:
    titanic = pd.read_csv(f, index_col=0)


filter1 = titanic.loc[(titanic['Age'] > 30)
                      & (titanic['Sex'] == 'male')
                     & (titanic['Pclass'])]
filter2 = titanic.loc[((titanic['Age'] < 18)
                      | (titanic['Sex'] == 'female'))
                      & (titanic['Survived'])]
