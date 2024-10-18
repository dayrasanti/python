import seaborn as sns
import matplotlib.pyplot as plt


# Cargar dataset
tips = sns.load_dataset("tips")

# Configuración del estilo y tamaño
sns.set_style("darkgrid")
plt.figure(figsize=(12, 8))

# Gráfico de dispersión con ajuste lineal
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="day", size="size")
sns.lineplot(x=tips["total_bill"], y=tips["tip"], color="red")

plt.title("Propinas vs. Total de Factura")
plt.show()