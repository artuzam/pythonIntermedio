import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Fecha": pd.date_range(start="2023-08-01", periods=7),
    "Producto": ["A", "B", "A", "C", "B", "C", "A"],
    "Cantidad": [10, 15, 8, 12, 5, 7, 11],
    "Precio Unitario": [100, 200, 150, 300, 180, 250, 120],
}

df = pd.DataFrame(data)
print(df)

# Estadísticas descriptivas
print("Estadísticas generales:")
# print(df.describe())

# Total de ventas
total_ventas = df["Cantidad"].sum()
print("Total de ventas:", total_ventas)

# Producto más vendido
producto_mas_vendido = df["Producto"].mode().values[0]
print("Producto más vendido:", producto_mas_vendido)

# Día con la mayor cantidad de ventas
dia_max_ventas = df.loc[df["Cantidad"].idxmax(), "Fecha"]
print("Día con la mayor cantidad de ventas:", dia_max_ventas)

# Agrupar datos por producto y sumar la cantidad vendida
ventas_por_producto = df.groupby("Producto")["Cantidad"].sum()
print(ventas_por_producto)

# Crear la gráfica de barras
plt.bar(ventas_por_producto.index, ventas_por_producto.values)
plt.xlabel("Producto")
plt.ylabel("Cantidad Vendida")
plt.title("Cantidad Vendida por Producto")
plt.show()
