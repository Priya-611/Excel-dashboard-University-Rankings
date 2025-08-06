import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("C:\\Users\\HP\\OneDrive\\Documents\\Project(Data Science)\\Excel\\university ranking\\THE World University Rankings 2016-2025.csv")
# print(df.head())
# print(df.info())
# print(df.describe())
# print(df.isnull().sum())
#female to male ratio 672 null

# print(df.dtypes)

df[['f', 'm']] = df['Female to Male Ratio'].astype(str).str.extract(r'(\d{1,3})\s*:\s*(\d{1,3})')


df['f'] = pd.to_numeric(df['f'], errors='coerce')
df['m'] = pd.to_numeric(df['m'], errors='coerce')
# errors=coerce,, if a value cannot be converted to a number, convert it to NaN (missing value) instead of raising an error

df['f']=df['f'].fillna(df.groupby('Country')['f'].transform('mean'))
df['m']=df['m'].fillna(df.groupby('Country')['m'].transform('mean'))


df['f']=df['f'].fillna(df['f'].mean())
df['m']=df['m'].fillna(df['m'].mean())



df['total'] = df['f'] + df['m']
df['Female'] = (df['f'] / df['total'])
df['Male'] = (df['m'] / df['total'])
df.drop(['f','m','total','Female to Male Ratio'],axis=1,inplace=True)
# print(df.head(10))
# print(df.isnull().sum())
# print(df[['Female to Male Ratio', 'Female', 'Male']].head(10))


df['International Students'] = df['International Students'].str.replace('%','',regex=False)
df['International Students']= pd.to_numeric(df['International Students'], errors='coerce')
df['International Students'] =df['International Students']/100   #(convert into decimal percentage)

# regex=False ,The string you pass is treated as a literal string. So '%' means just the percent sign, nothing special.

# print(df['International Students'])

df.to_excel("C:\\Users\\HP\\OneDrive\\Documents\\Project(Data Science)\\Excel\\university ranking\\Cleaned_University_Ranking.xlsx", index=False)
 