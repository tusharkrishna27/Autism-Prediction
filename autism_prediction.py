# -*- coding: utf-8 -*-
"""AUTISM PREDICTION

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1g_cTr9YBU6WSzmLBogXUX7BrChRB-AH7
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn import metrics
from sklearn.svm import SVC
from xgboost import XGBClassifier
from sklearn.linear_model import LogisticRegression
from imblearn.over_sampling import RandomOverSampler

import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('/test.csv')
print(df.head())

df.shape

df.info()

df.describe().T

df['jaundice'].value_counts()

df['relation'].value_counts()

df = df.replace({'yes':1, 'no':0, '?':'Others', 'others':'Others'})

# Verify the column names in your DataFrame
print(df.columns)

# Replace 'Class_ASD' with the actual column name for the ASD class
plt.pie(df['<Actual Column Name>'].value_counts().values, autopct='%1.1f%%')
plt.show()

ints = []
objects = []
floats = []

for col in df.columns:
  if df[col].dtype == int:
    ints.append(col)
  elif df[col].dtype == object:
    objects.append(col)
  else:
    floats.append(col)

# Check if 'Class/ASD' is in the list before removing
if 'Class/ASD' in ints:
    ints.remove('Class/ASD')