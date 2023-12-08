# Importar
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# Leer
df = pd.read_csv('supermarket_sales.csv')

# Convertir columna date a fecha y hora
df['Date'] = pd.to_datetime(df['Date'])

# Nueva columna 'Mes' extrayendo el mes de la columna date
df['Mes'] = df['Date'].dt.month

# Agrupe los datos por 'Branch' y 'Mes' y calcular las ventas de la columna 'Total' para cada grupo
grupos = df.groupby(['Branch', 'Mes'])['Total'].sum()

# Calcular la tasa de cricimiento mensual de cada 'Branch'
grouped = df.groupby(['Branch', 'Mes'])['Total'].sum()
growth_rate = grouped.groupby(level=0).pct_change()

# Cree un grafico de lineas a partir de la informacion anterior
def graficoLineas_tasaCrecimiento():
    growth_rate.unstack(level=0).plot(kind='line')
    plt.show()

# Agrupar los datos por 'Branch' y calcular las ventas totales, la calificacion promedio y calificacion maxima para cada sucursal
grupo_t = df.groupby(['Branch'])['Total'].sum()
grupo_p = df.groupby(['Branch'])['Rating'].mean()
grupo_m = df.groupby(['Branch'])['Rating'].max()
gruposS = grupo_m, grupo_p, grupo_t

# Identificar la sucursal con las ventas mas altas e imprima sus detalles, incluido el nombre de la sucursal y las ventas totales
grouped = df.groupby('Branch')['Total'].sum()
max_sales = grouped.idxmax()
max_sales_value = grouped.loc[max_sales]

# Identificar la sucursal con la calificacion promedio mas alta e imprimir sus detalles, incluido el nombre el nombre de la sucursal y las ventas totales
grouped_rp = df.groupby('Branch')['Rating'].mean()
max_rate_p = grouped_rp.idxmax()
max_sales_value_r_p = grouped_rp.loc[max_rate_p]

# Identificar la sucursal con la calificacion maxima e imprimir sus detalles, incluido el nombre de la sucursal y las ventas totales
grouped_r = df.groupby('Branch')['Rating'].sum()
max_rate = grouped_r.idxmax()
max_sales_value_r = grouped_r.loc[max_rate]

# Imprimir las 5 ciudades principales con las ventas totales mas altas
df_c = df.groupby('City')['Total'].sum().head(5).sort_values(ascending=False)

# Imprimir los ingresos totales de cada linea de productos
df_i = df.groupby('Product line')['Total'].sum()

# Agrupar los datos por 'Ciudad', 'Tipo de cliente' y 'Género' y calcular los ingresos totales para cada grupo
df_ig = df.groupby(['City', 'Customer type', 'Gender'])['Total'].sum()

# Gráfico de barras apiladas para visualizar la distribución de ingresos en diferentes ciudades, agrupadas por tipo de cliente y género.
def graficoBarras_ciudades():
    df_i.plot(kind='bar', stacked=True, title='Ingresos totales en ciudades, tipos de clientes, y géneros')
    plt.xlabel('Ciudad, tipos de clientes, y géneros')
    plt.ylabel('Ingresos totales')
    plt.xticks(rotation=45)
    plt.show()

# Establecer la columna 'Date' como el índice del DataFrame.
df.set_index('Date', inplace=True)

# Volver a muestrear los datos con una frecuencia mensual y calcular los ingresos totales de cada mes.
ingresos = df.resample('M').sum()['Total']

def graficoPrediccion():
    # Realizar una descomposición de series de tiempo usando un método adecuado para separar los datos de ingresos en sus componentes 
    # estacionales, de tendencia y residuales.
    model = ARIMA(ingresos, order=(1, 1, 1))
    model_fit = model.fit()
    predictions = model_fit.predict(start='2019-03', end='2023-12', dynamic=True)

    # Gráfico de descomposición para visualizar la estacionalidad, la tendencia y los componentes residuales de los datos de 
    # ingresos
    plt.figure(figsize=(10, 6))
    plt.plot(ingresos, label='Ingresos reales')
    plt.plot(predictions, label='Predicciones')
    plt.title('Predicciones de ingresos anuales')
    plt.xlabel('Fecha')
    plt.ylabel('Ingresos')
    plt.legend()
    plt.show()

# Programa principal
seguir_en_programa = True
while seguir_en_programa == True: 
    print("") 
    print("### BIENVENIDO ###") 
    print("Que desea hacer?") 
    print("1. Ver las ventas totales de los datos agrupados por mes y branch") 
    print("2. Ver tasa de cricimiento mensual de cada branch") 
    print("3. Ver grafico de lineas de la tasa de crecimiento") 
    print("4. Ver ventas totales, calificacion promedio y calificacion maxima de cada sucursal") 
    print("5. Ver sucursal con las ventas mas altas") 
    print("6. Ver la sucursal con la calificacion promedio mas alta") 
    print("7. Ver la sucursal con la calificacion mas alta") 
    print("8. Ver las 5 ciudades principales con las ventas totales mas altas")
    print("9. Ver los ingresos totales de cada linea de productos")
    print("10. Los ingresos totales de cada grupo")
    print("11. Ver un gráfico de barras apiladas de la distribución de ingresos en diferentes ciudades, agrupadas por tipo de cliente y género")
    print("12. Ver los ingresos totales de cada mes")
    print("13. Ver grafico con las predicciones de ingresos anuales")
    print("14. Salir")

    opcion = input("Seleccione una opción válida ") 

    # Hacer que la opción elegida sea un dígito, y si no lo es, volver a ejecutar el menú 
    if opcion.isdigit() == False: 
        print("Seleccione un tipo de valor válido") 
    else: 
        opcion = int(opcion) 

    if opcion == 1:
        print("")
        print(grupos)

    if opcion == 2:
        print("")
        print(growth_rate)
    
    if opcion == 3:
        graficoLineas_tasaCrecimiento()
    
    if opcion == 4:
        print("")
        print(gruposS)

    if opcion == 5:
        print("")
        print(f'La sucursal con las ventas mas altas es {max_sales} Con un total de ventas de {max_sales_value:.2f}')

    if opcion == 6:
        print("")
        print(f'La sucursal con la calificacion promedio mas altas es {max_rate_p} Con un total de ventas de {max_sales_value_r_p:.2f}')

    if opcion == 7:
        print("")
        print(f'La sucursal con la calificacion mas alta es {max_rate} Con un total de ventas de {max_sales_value_r:.2f}')

    if opcion == 8:
        print("")
        print(f'Las 5 ciudades principales con las ventas mas altas son: \n{df_c}')
    
    if opcion == 9:
        print("")
        print(f'Los ingresos totales de cada linea de productos son: \n{df_i}')

    if opcion == 10:
        print("")
        print(f'Los ingresos totales para cada grupo son: \n{df_ig}')

    if opcion == 11:
        graficoBarras_ciudades()

    if opcion == 12:
        print(f"\nlos ingresos totales de cada mes son: \n{ingresos}")
    
    if opcion == 13:
        graficoPrediccion()
    
    if opcion == 14:
        seguir_en_programa = False
        print("Eso ha sido todo, vuelva pronto!")        
    else:
        print("Seleccione una opción válida.")    