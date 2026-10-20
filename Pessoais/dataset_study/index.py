import seaborn as sns
import pandas as pd
import scipy.stats as stats
import time
pd.options.display.float_format = '{:.2f}'.format

df = sns.load_dataset("tips")
#tratando colunas
colunas_texto = ['sex', 'smoker']
df[colunas_texto] = df[colunas_texto].astype('category').apply(lambda x: x.cat.codes)
print(df.head(10))
'''
df["sex"] = df["sex"].map({'Female': 1, 'Male': 0})
df["smoker"] = df["smoker"].map({'Yes': 1, 'No': 0})
df["day"] = df["day"].astype('category').cat.codes
print(df["sex"].head())
print(df["smoker"].head())
print(df["day"].head())
#pearson = df.corr(method='pearson')
#print(pearson)
'''
pearson = df.corr(method='pearson')
print(pearson)