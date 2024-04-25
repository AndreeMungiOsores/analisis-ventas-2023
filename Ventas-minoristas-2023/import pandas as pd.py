import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el conjunto de datos CSV
ventas = pd.read_csv('ventas_minoristas.csv')

# Convertir la columna de fecha a formato datetime
ventas['Fecha_Venta'] = pd.to_datetime(ventas['Fecha_Venta'])

# Agregar columnas para el mes y el año de la venta
ventas['Mes_Venta'] = ventas['Fecha_Venta'].dt.month
ventas['Año_Venta'] = ventas['Fecha_Venta'].dt.year

# Calcular las ventas mensuales y anuales
ventas_mensuales = ventas.groupby(['Año_Venta', 'Mes_Venta'])['Total_Venta'].sum().reset_index()
ventas_anuales = ventas.groupby(['Año_Venta'])['Total_Venta'].sum().reset_index()

# Visualizar las ventas mensuales y anuales
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
sns.lineplot(data=ventas_mensuales, x='Mes_Venta', y='Total_Venta', hue='Año_Venta', marker='o')
plt.title('Ventas Mensuales')
plt.xlabel('Mes')
plt.ylabel('Total de Ventas')
plt.savefig('ventas_mensuales.png')  # Guardar la imagen como archivo PNG

plt.subplot(1, 2, 2)
sns.barplot(data=ventas_anuales, x='Año_Venta', y='Total_Venta', hue='Año_Venta', palette='viridis', legend=False)
plt.title('Ventas Anuales')
plt.xlabel('Año')
plt.ylabel('Total de Ventas')
plt.tight_layout()
plt.savefig('ventas_anuales.png')  # Guardar la imagen como archivo PNG
plt.close()  # Cerrar la figura para liberar memoria

# Gráfico de dispersión de precio unitario vs. cantidad vendida
plt.figure(figsize=(8, 6))
sns.scatterplot(data=ventas, x='Precio_Unitario', y='Cantidad_Vendida', hue='Categoria_Producto')
plt.title('Precio Unitario vs. Cantidad Vendida')
plt.xlabel('Precio Unitario')
plt.ylabel('Cantidad Vendida')
plt.legend(title='Categoría de Producto')
plt.savefig('scatterplot_precio_cantidad.png')  # Guardar la imagen como archivo PNG
plt.close()  # Cerrar la figura para liberar memoria

# Matriz de correlación
correlation_matrix = ventas[['Precio_Unitario', 'Cantidad_Vendida', 'Total_Venta']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Matriz de Correlación')
plt.savefig('matriz_correlacion.png')  # Guardar la imagen como archivo PNG
plt.close()  # Cerrar la figura para liberar memoria

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Seleccionar las características relevantes para el análisis de segmentación de clientes
features = ['Precio_Unitario', 'Cantidad_Vendida', 'Total_Venta']

# Escalar las características
scaler = StandardScaler()
ventas_scaled = scaler.fit_transform(ventas[features])

# Aplicar K-means para la segmentación de clientes
kmeans = KMeans(n_clusters=3, random_state=42)
ventas['Cluster'] = kmeans.fit_predict(ventas_scaled)

# Visualizar la segmentación de clientes
plt.figure(figsize=(8, 6))
sns.scatterplot(data=ventas, x='Precio_Unitario', y='Cantidad_Vendida', hue='Cluster', palette='Set1')
plt.title('Segmentación de Clientes')
plt.xlabel('Precio Unitario')
plt.ylabel('Cantidad Vendida')
plt.savefig('segmentacion_clientes.png')  # Guardar la imagen como archivo PNG
plt.close()  # Cerrar la figura para liberar memoria
