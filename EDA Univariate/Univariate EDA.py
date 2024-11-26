import pandas as pd
import numpy as np
import seaborn as sns

df = pd.read_csv("G:/Coding/Programs/Machine Learning/Data/train.csv")

print(df.head())

# categorical Data 

print(sns.countplot(df['Survived']))