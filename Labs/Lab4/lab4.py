import pandas as pd
import matplotlib.pyplot as plt

# leer archivo CSV
df = pd.read_csv("ventas.csv")

# Calcular el beneficio mensual restando los gastos a las ventas y agregarlo como una nueva columna.
df["Ganancia"] = df["Ventas"] - df["Gastos"]

# Graficar la evolución mensual de las ventas y los gastos en un gráfico de líneas.
plt.figure(figsize=(10, 6))
plt.plot(df["Mes"], df["Ventas"], label="Ventas", marker="d")
plt.plot(df["Mes"], df["Gastos"], label="Gastos", marker="o")
plt.plot(df["Mes"], df["Ganancia"], label="Ganancia", marker="s")

# Agregar etiquetas y título al gráfico.
plt.xlabel("Mes")
plt.ylabel("Cantidad")
plt.title("Evolución Mensual de Ventas y Gastos")
plt.grid(True)
plt.xticks(fontsize=8)  # tamaño del texto del 'tick'

# Agregar una leyenda que indique las líneas correspondientes a las ventas y los gastos.
plt.legend()

# Mostrar el gráfico.
plt.show()
