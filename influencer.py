import pandas as pd
import numpy as np

df=pd.read_excel("C:\\Users\\srave\\OneDrive\\Desktop\\jupyter\\Influencer.xlsx")
print(df.head(3))
print(df.info())
print(df.isnull().sum())
print(df.shape)
print(df.columns)
print(df.describe())
print(df.duplicated().sum())

influence=np.array(df['Influence Score'])
print(influence)
print(np.mean(influence))
print(np.max(influence))
print(np.min(influence))
print(np.var(influence))
print(np.std(influence))

a=np.array(df['Influence Score'])
print(a+5)
print(a*5)
print(a-5)