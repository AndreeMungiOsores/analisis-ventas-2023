import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Cargar el conjunto de datos CSV existente
marketing = pd.read_csv('marketing_complejo.csv')
print(marketing.head())  # Verificar que se haya cargado correctamente

# Directorio de salida para los archivos PNG
output_dir = 'graficos_marketing'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Mapa de calor de ingresos por producto y canal publicitario
heatmap_data = marketing.pivot_table(index='Producto', columns='Canal_Publicitario', values='Ingresos', aggfunc='sum')
plt.figure(figsize=(10, 8))
sns.heatmap(heatmap_data, cmap='viridis', annot=True, fmt=".0f", cbar=True)
plt.title('Mapa de Calor de Ingresos por Producto y Canal Publicitario')
plt.xlabel('Canal Publicitario')
plt.ylabel('Producto')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'mapa_calor_ingresos.png'))  # Guardar el gráfico como PNG
plt.close()
print("Mapa de calor guardado")

# Diagrama de dispersión de ingresos vs. clientes alcanzados
plt.figure(figsize=(8, 6))
sns.scatterplot(data=marketing, x='Clientes_Alcance', y='Ingresos')
plt.title('Ingresos vs. Clientes Alcanzados')
plt.xlabel('Clientes Alcanzados')
plt.ylabel('Ingresos')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'ingresos_vs_clientes.png'))  # Guardar el gráfico como PNG
plt.close()
print("Diagrama de dispersión guardado")

# Gráfico de barras apiladas de ingresos por categoría de producto y segmento de cliente
stacked_bar_data = marketing.groupby(['Categoria', 'Segmento_Cliente'])['Ingresos'].sum().unstack()
stacked_bar_data.plot(kind='bar', stacked=True, figsize=(10, 6))
plt.title('Ingresos por Categoría de Producto y Segmento de Cliente')
plt.xlabel('Categoría de Producto')
plt.ylabel('Ingresos')
plt.xticks(rotation=45)
plt.legend(title='Segmento de Cliente')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'ingresos_por_categoria_segmento.png'))  # Guardar el gráfico como PNG
plt.close()
print("Gráfico de barras apiladas guardado")

# Gráfico de líneas múltiples de ingresos por producto a lo largo del tiempo
line_plot_data = marketing.pivot_table(index='Fecha', columns='Producto', values='Ingresos', aggfunc='sum')
plt.figure(figsize=(10, 6))
line_plot_data.plot(ax=plt.gca())
plt.title('Ingresos por Producto a lo largo del Tiempo')
plt.xlabel('Fecha')
plt.ylabel('Ingresos')
plt.xticks(rotation=45)
plt.legend(title='Producto')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'ingresos_por_producto.png'))  # Guardar el gráfico como PNG
plt.close()
print("Gráfico de líneas múltiples guardado")

# Diagrama de violín de clientes alcanzados por segmento de cliente y canal publicitario
violin_data = marketing[['Segmento_Cliente', 'Canal_Publicitario', 'Clientes_Alcance']]
plt.figure(figsize=(10, 6))
sns.violinplot(data=violin_data, x='Segmento_Cliente', y='Clientes_Alcance', hue='Canal_Publicitario', split=True)
plt.title('Distribución de Clientes Alcanzados por Segmento de Cliente y Canal Publicitario')
plt.xlabel('Segmento de Cliente')
plt.ylabel('Clientes Alcanzados')
plt.legend(title='Canal Publicitario')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'clientes_alcanzados_segmento.png'))  # Guardar el gráfico como PNG
plt.close()
print("Diagrama de violín guardado")
