# -*- coding: utf-8 -*-
"""Untitled8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_g0as1VLBpeQWj2xC2P2u2kScLw5I1na

# Comparison of Classifiers
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.naive_bayes import GaussianNB

names = [
"K-Nearest Neighbors",
"Linear SVM",
"Decision Tree",
"Multilayer Perceptron",
"Gaussian Naive Bayes",
]

classifiers = [
KNeighborsClassifier(3),
SVC (kernel="linear", C=0.025),
DecisionTreeClassifier (max_depth=5),
MLPClassifier (alpha=1, max_iter=1800),
GaussianNB(),
]

df = pd.read_csv("/content/Iris.csv")

df.head()

df = df.drop("Id", axis= 1)

df.head()

#Extract X and y as features and target
X= df.iloc[:, :-1]
X.head()

y= df.iloc[:, -1]
y.head()

#Since target column is categorical, we will convert it to numerical usign LabelEncoder
from sklearn.preprocessing import LabelEncoder

y = LabelEncoder().fit_transform(y)
y= pd.DataFrame(y)

y.head()

#Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

#Using a for loop fit all the classifiers to X_train and y_train and print the accuracy score of each classifier

for name, clf in zip(names, classifiers):
    clf.fit(X_train, y_train.values.ravel())
    score = clf.score (X_test, y_test)
    print("Classifier Name: ", name, "Score: ", score)

