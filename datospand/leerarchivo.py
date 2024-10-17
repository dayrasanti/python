import pandas as pd


df=pd.read_csv("poblacion.csv")
# print(df.head())
# print(df.describe())
# print(df.tail())
# print(df.sample())
# print(df[["Date", "COL", "ARG"]])

# # filtrado de datos
# filtro = df[df['COL'] > 30000]
# print(filtro)
# Añadir una columna


# Eliminar una columna
df = df.drop(columns=['ABW'])

print(df)