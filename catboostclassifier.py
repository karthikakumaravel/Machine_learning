# -*- coding: utf-8 -*-
"""catboostclassifier.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19ig0D8svUGbWTnrmxwnE2pPaVhswAlXi
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn

!pip install catboost
import catboost

train=pd.read_csv("https://raw.githubusercontent.com/ezioauditore-tech/AI/main/datasets/amazon-employee-access-challenge/train.csv")
test=pd.read_csv("https://raw.githubusercontent.com/ezioauditore-tech/AI/main/datasets/amazon-employee-access-challenge/test.csv")

train

test #in test no dependent variable so need to take train itself

train.shape

test.shape

from catboost import CatBoostClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

#train=train.iloc[:,:-1].values #his selects all columns up to, but not including, the last column.
#train=train.iloc[:,-1].values

x=train.drop("ACTION",axis=1)
y=train["ACTION"]

cat_feat=list(range(0,x.shape[1]))
print(cat_feat)

x, X_test, y, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Create a CatBoostClassifier instance
model = CatBoostClassifier(iterations=100,  # specify the number of boosting iterations
                           learning_rate=0.1,  # specify the learning rate
                           depth=6,  # specify the depth of the trees
                           loss_function='Logloss',  # specify the loss function
                           random_seed=42)  # set a random seed for reproducibility

# Train the model on the training data
model.fit(x, y, eval_set=(X_test, y_test), early_stopping_rounds=10, verbose=10)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")