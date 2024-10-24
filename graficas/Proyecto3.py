# import matplotlib.pyplot as plt
# import pandas as pd

# # Cargar los datos

# df=pd.read_csv("1.csv")

# # Filtrar por año y departamento
# filtro = df[df['AÑO'] > 2014]
# filtro2 = filtro[filtro['DEPARTAMENTO'] == 'Santander']

# # Variables para el gráfico
# x = filtro2['AÑO']
# z = filtro2["COBERTURA_NETA"]
# t = filtro2["SEDES_CONECTADAS_A_INTERNET"]

# # Crear gráfica lineal
# plt.plot(x, z, label="Cobertura Neta", marker='o')
# plt.plot(x, t, label="Sedes Conectadas a Internet", marker='s')

# # Etiquetas y título
# plt.xlabel("Año")
# plt.ylabel("Cantidad")
# plt.title("Cobertura Neta y Sedes Conectadas a Internet en Santander")
# plt.legend()

# # Mostrar gráfica
# plt.show()
import matplotlib.pyplot as plt
import pandas as pd

# Cargar el archivo CSV desde la carpeta "graficas"
file_path = 'graficas/1.csv'
try:
    df = pd.read_csv(file_path)
    print("Archivo CSV cargado correctamente.")
except Exception as e:
    print(f"Error al leer el archivo CSV: {e}")
    exit()

# # # Obtener los nombres únicos de los departamentos
# departamentos = df['DEPARTAMENTO'].unique()

# # # Crear la gráfica de la tasa de matriculación para cada departamento
# plt.figure(figsize=(10, 6))  # Ajustar el tamaño de la figura

# for departamento in departamentos:
#     filtro_dep = df[df['DEPARTAMENTO'] == departamento]
#     plt.plot(filtro_dep['AÑO'], filtro_dep['DESERCIÓN'], label=departamento, marker='o')

# # Etiquetas y título
# plt.xlabel("Año")
# plt.ylabel("Tasa de Matriculación (%)")
# plt.title("Tasa de Matriculación 5-16 años por Departamento (Todos los Años)")
# plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')  # Ubicación de la leyenda fuera de la gráfica
# plt.tight_layout()  # Ajustar el layout para que no se corten las etiquetas
# plt.show()



departamentos_filtrados = ['Córdoba', 'Bogotá, D.C.', 'Huila','Tolima','Caquetá','Nariño','Putumayo', 'Archipiélago de San Andrés, Providencia y Santa Catalina']
filtro_departamentos = df[df['DEPARTAMENTO'].isin(departamentos_filtrados)]

# Crear la gráfica de la tasa de matriculación para estos departamentos
plt.figure(figsize=(10, 6))  # Ajustar el tamaño de la figura

for departamento in departamentos_filtrados:
    filtro_dep = filtro_departamentos[filtro_departamentos['DEPARTAMENTO'] == departamento]
    # plt.plot(filtro_dep['AÑO'], filtro_dep['TASA_MATRICULACIÓN_5_16'], label=departamento, marker='o')
    plt.plot(filtro_dep['AÑO'], filtro_dep['DESERCIÓN'], label=departamento, marker='o')

# Etiquetas y título
plt.xlabel("Año")
plt.ylabel("Desercion (%)")
plt.title("Tasa de Desercion")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')  # Ubicación de la leyenda fuera de la gráfica
plt.tight_layout()  # Ajustar el layout para que no se corten las etiquetas
plt.show()