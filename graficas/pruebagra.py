import matplotlib.pyplot as plt
import pandas as pd
# x = [1, 2, 3, 4]
# y = [1, 4, 9, 16]

# plt.plot(x, y)
# plt.xlabel('Eje X')
# plt.ylabel('Eje Y')
# plt.title('Gráfico simple de Matplotlib')
# plt.show() 
# categorias = ['A', 'B', 'C', 'D']
# valores = [3, 7, 1, 8]

# plt.bar(categorias, valores)
# plt.xlabel('Categorías')
# plt.ylabel('Valores')
# plt.title('Gráfico de barras')
# plt.show()
df=pd.read_csv("poblacion.csv")
x = df["Date"]
y = df["COL"]
z= df["AFG"]
t= df["ARG"]

plt.plot(x, y)
plt.plot(x, z)
plt.plot(x, t)
plt.xlabel('Fecha')
plt.ylabel('poblacion')

plt.title('Gráfico con estilo personalizado')
plt.show()