import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el conjunto de datos desde el archivo CSV
datos_salud_publica = pd.read_csv('datos_salud_publica_peru.csv')

# Visualización de la cantidad de casos de influenza, neumonía y dengue a lo largo del año
plt.figure(figsize=(12, 6))
sns.lineplot(data=datos_salud_publica, x='Mes', y='Casos_Influenza', label='Influenza')
sns.lineplot(data=datos_salud_publica, x='Mes', y='Casos_Neumonia', label='Neumonía')
sns.lineplot(data=datos_salud_publica, x='Mes', y='Casos_Dengue', label='Dengue')
plt.title('Casos de Enfermedades a lo largo del Año')
plt.xlabel('Mes')
plt.ylabel('Cantidad de Casos')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig('casos_enfermedades.png')
plt.show()

# Visualización de la población estimada y las camas de hospital disponibles a lo largo del año
plt.figure(figsize=(12, 6))
plt.plot(datos_salud_publica['Mes'], datos_salud_publica['Poblacion'], marker='o', label='Población')
plt.plot(datos_salud_publica['Mes'], datos_salud_publica['Camas_Hospital'], marker='o', label='Camas de Hospital')
plt.title('Población Estimada vs. Camas de Hospital Disponibles')
plt.xlabel('Mes')
plt.ylabel('Cantidad')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig('poblacion_camas_hospital.png')
plt.show()

# Visualización del personal de salud a lo largo del año
plt.figure(figsize=(12, 6))
plt.plot(datos_salud_publica['Mes'], datos_salud_publica['Personal_Medico'], marker='o', label='Personal Médico')
plt.plot(datos_salud_publica['Mes'], datos_salud_publica['Personal_Enfermeria'], marker='o', label='Personal de Enfermería')
plt.title('Personal de Salud a lo largo del Año')
plt.xlabel('Mes')
plt.ylabel('Cantidad')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig('personal_salud.png')
plt.show()

# Visualización de las vacunas aplicadas a lo largo del año
plt.figure(figsize=(12, 6))
plt.plot(datos_salud_publica['Mes'], datos_salud_publica['Vacunas_Aplicadas'], marker='o')
plt.title('Vacunas Aplicadas a lo largo del Año')
plt.xlabel('Mes')
plt.ylabel('Cantidad de Vacunas Aplicadas')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('vacunas_aplicadas.png')
plt.show()
