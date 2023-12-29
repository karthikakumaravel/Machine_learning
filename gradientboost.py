# -*- coding: utf-8 -*-
"""gradientboost.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ndy4H3Iy_x80jjD7e29YnEo2YHc38Yk_
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

train=pd.read_csv("https://raw.githubusercontent.com/ezioauditore-tech/AI/main/datasets/Titanic/train.csv")
test=pd.read_csv("https://raw.githubusercontent.com/ezioauditore-tech/AI/main/datasets/Titanic/test.csv")

test.isnull().sum()

train.info()

test.info()

train.set_index("PassengerId",inplace=True)
test.set_index("PassengerId",inplace=True)



y_train=train["Survived"] #drop

train.drop(labels="Survived",axis=1,inplace=True)

train.shape

"""combining train and test -->  we need more data so combining train and test"""

train_test=train.append(test)

col_drop=["Name","Age","SibSp","Ticket","Fare","Cabin","Embarked"]
train_test.drop(labels=col_drop,axis=1,inplace=True)

train_test_dummies=pd.get_dummies(train_test,columns=["Sex"]) #like one hot encoder it performs

train_test_dummies.isnull().sum()

train_test_dummies.fillna(value=0.0,inplace=True)

"""splitting train and test"""

x_train=train_test_dummies.values[0:891]
x_test=train_test_dummies.values[891:]

"""fare value is more
so we are using standard scaler
"""

from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler()
x_train_scale=scaler.fit_transform(x_train)
x_test_scale=scaler.transform(x_test) #fit use -->already fitsso no need to five fit

from sklearn.model_selection import train_test_split
x_tr_sub,x_val_sub,y_tr_sub,y_val_sub=train_test_split(x_train_scale,y_train,random_state=0)

from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import classification_report,confusion_matrix

learning_rates=[0.05,0.1,0.25,0.5,0.75,1]
for learning_rate in learning_rates:
  gb=GradientBoostingClassifier(n_estimators=20,learning_rate=learning_rate,max_features=2,max_depth=2,random_state=0)
  gb.fit(x_tr_sub,y_tr_sub)
  print("learning rate",learning_rate)
  print("accuracy score(training): {0:.3f}".format(gb.score(x_tr_sub,y_tr_sub)))
  print("accuracy score(validation):{0:.3f}".format(gb.score(x_val_sub,y_val_sub)))
  print()