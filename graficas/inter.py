import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk

# Cargar los datos desde el archivo CSV
df = pd.read_csv("poblacion.csv")

# Crear la ventana principal de Tkinter
root = tk.Tk()
root.title("Gráfico de Población por País")

# Crear una lista desplegable de países
paises = df.columns[1:]  # Excluimos la columna 'Date'

# Crear un marco para el gráfico
frame_grafico = tk.Frame(root)
frame_grafico.pack(pady=20)

# Función para actualizar el gráfico basado en el país seleccionado
def actualizar_grafico(event):
    pais_seleccionado = combo_paises.get()
    df_filtrado = df[['Date', pais_seleccionado]]
    
    # Crear la figura de Matplotlib
    fig, ax = plt.subplots(figsize=(8,6))
    ax.plot(df_filtrado['Date'], df_filtrado[pais_seleccionado], marker='o', label=pais_seleccionado)
    ax.set_title(f"Población de {pais_seleccionado}")
    ax.set_xlabel("Año")
    ax.set_ylabel("Población")
    ax.grid(True)
    
    # Limpiar el marco anterior si ya se ha mostrado un gráfico
    for widget in frame_grafico.winfo_children():
        widget.destroy()
    
    # Crear el canvas para mostrar el gráfico en Tkinter
    canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Crear una etiqueta y un combobox para seleccionar el país
lbl_pais = tk.Label(root, text="Selecciona un país:")
lbl_pais.pack(pady=10)

combo_paises = ttk.Combobox(root, values=paises)
combo_paises.set("Selecciona un país")
combo_paises.pack(pady=5)

# Asignar la función actualizar_grafico al cambio en la selección del país
combo_paises.bind("<<ComboboxSelected>>", actualizar_grafico)

# Ejecutar la ventana de Tkinter
root.mainloop()