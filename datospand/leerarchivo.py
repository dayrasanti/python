import pandas as pd


df=pd.read_csv("poblacion.csv")
print(df.head())
print(df.describe())
print(df.tail())
print(df.sample())