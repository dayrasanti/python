import matplotlib.pyplot as plt
import pandas as pd

# Cargar los datos
df = pd.read_csv("1.csv")

# Filtrar por año y departamento
filtro = df[df['AÑO'] > 2014]
filtro2 = filtro[filtro['DEPARTAMENTO'] == 'Santander']

# Variables para el gráfico
x = filtro2['AÑO']
z = filtro2["COBERTURA_NETA"]
t = filtro2["SEDES_CONECTADAS_A_INTERNET"]

# Crear gráfica lineal
plt.plot(x, z, label="Cobertura Neta", marker='o')
plt.plot(x, t, label="Sedes Conectadas a Internet", marker='s')

# Etiquetas y título
plt.xlabel("Año")
plt.ylabel("Cantidad")
plt.title("Cobertura Neta y Sedes Conectadas a Internet en Santander")
plt.legend()

# Mostrar gráfica
plt.show()