# Se empieza a realizar el llamado a cada modulo.
from api.api import ClienteAPI
from datos.gestor_datos import GestorDatos
from eda.procesador_eda import ProcesadorEDA as eda
from basedatos.gestor_basedatos import BD
from modelos.modelo_ml import ModeloML
from helpers.utilidades import Utilidades
from visualizacion.visualizador import visualizador
import pandas as pd

#PARAMETROS PARA VER LOS df COMPLETOS SIN CORTES
#pd.set_option("display.max_rows", None)
#pd.set_option("display.max_columns", None)

""""
#----------------------------------------------------------------------------------------------------------------------#
# Clase = ClienteAPI / Instancia para consultar las API's
cliente_api = ClienteAPI()
cliente_api.coordenadas_paises()
cliente_api.clima_anual(2013, lat=10, lon=-84)
cliente_api.clima_rango_anios(2013, 2024, lat=10, lon=-84)

#----------------------------------------------------------------------------------------------------------------------#
# Clase = GestorDatos / Instancia para cargar los datos
turismo = GestorDatos('data/raw/turismo_anios.csv')
# Se llama al metodo de la clase para leer el archivo
turismo.leer_archivo()

zonas = GestorDatos('data/raw/zonas_aerea.csv')
zonas.leer_archivo()

#----------------------------------------------------------------------------------------------------------------------#
# Clase = ProcesadorEDA / Instacia para poder limpiar el csv.
eda_turismo = eda(turismo.df)
eda_turismo.ejecutar_eda('turismo_anios_clean.csv')

eda_zonas = eda(zonas.df)
eda_zonas.ejecutar_eda('zonas_aereas_clean.csv')

"""

"""
#----------------------------------------------------------------------------------------------------------------------#
#Ejecucion base datos(Actualizacion)

#Carga de los archivos CSV processed

#Archivo clima_anual_2013.csv
clima_anual=GestorDatos('data/processed/clima_anual_2013.csv')
df_clima_anual=pd.DataFrame(clima_anual.retornar_csv())

#Archivo clima_resumen_anual.csv
clima_resumen_anual=GestorDatos('data/processed/clima_resumen_anual.csv')
df_clima_resumen=pd.DataFrame(clima_resumen_anual.retornar_csv())


#Archivo Coordenadas_paises.csv
paises=GestorDatos('data/processed/Coordenadas_paises.csv')
df_paises=pd.DataFrame(paises.retornar_csv())


#Archivo turismo_anios_clean.csv
turismo_anual=GestorDatos('data/processed/turismo_anios_clean.csv')
df_turismo_anual=pd.DataFrame(turismo_anual.retornar_csv())


#Archivo zonas_aereas_clean.csv
zonas_aereas=GestorDatos('data/processed/zonas_aereas_clean.csv')
df_zonas_aereas=pd.DataFrame(zonas_aereas.retornar_csv())

#----------------------------------------------------------------------------------------------------------------------#
#Creacion base datos
basedatos=BD("MigracionCR")
basedatos.crear_tabla()

#----------------------------------------------------------------------------------------------------------------------#
#Insert de las tablas
#Tabla Paises
basedatos.insertar_paises(df_paises)

#Tabla Clima
basedatos.insertar_clima(df_clima_resumen,44)

#Tabla MedioIngreso
basedatos.insertar_medios_ingreso()

#Tabla Total_Ingresos_Anuales
#Limpieza CSV turismo_anios_clean  --df_turismo_anual
limpieza=basedatos.limpiar_dataframe_turismo(df_turismo_anual)
basedatos.insertar_total_ingresos_anuales(limpieza)
#----------------------------------------------------------------------------------------------------------------------#
#Consulta de las tablas

#Consulta Tabla Pais
consulta_pais=basedatos.consultar_tabla('Pais')
print(f"Tabla Pais \n {consulta_pais}")

#Consulta Tabla Clima Anual Costa Rica
consulta_clima=basedatos.consultar_tabla('Clima')
print(f"Tabla Clima Anual CR \n {consulta_clima}")

#Consulta Tabla MedioIngreso
consulta_medioIngreso=basedatos.consultar_tabla('MedioIngreso')
print(f"Tabla MedioIngreso \n {consulta_medioIngreso}")

#Consulta Total_Ingresos_Anuales
consulta_Registro=basedatos.consultar_tabla('Total_Ingresos_Anuales')
print(f"Tabla Total_Ingresos_Anuales \n {consulta_Registro}")

"""

#----------------------------------------------------------------------------------------------------------------------#
# Clase: Modelo ML / Instancia para crear nuestros modelo de prediccion.

# Define de funcion principal
def main():

    # Carga datos
    df_turismo = Utilidades.cargar_csv("../data/processed/turismo_anios_clean.csv")
    df_clima = Utilidades.cargar_csv("../data/processed/clima_resumen_anual.csv")

    if df_turismo is None or df_clima is None:
        print("No se pudieron cargar los CSV.")
        return

    # Prepara clima, seleccionando los las columnas a utilizar del df
    df_clima_anual = df_clima[["year", "temp_avg"]].rename(columns={
        "year": "ANNIOS",
        "temp_avg": "temperatura_promedio"
    })

   # combina turismo y clima
    df_merged = df_turismo.merge(df_clima_anual, on="ANNIOS", how="left")

    # hace una limpieza por si habia algo
    df_merged = df_merged.replace(r"\s+", "", regex=True)

    for col in df_merged.columns: # convierte en numerico
        df_merged[col] = pd.to_numeric(df_merged[col], errors="coerce") #mantiene dato original y no lanza error

    df_merged = df_merged.fillna(0) # remplaza nulos por 0

    print("\nDatos listos:")
    print(df_merged.head()) # muestra las primeras 5 filas listas

    # Entrenar modelos
    modelo = ModeloML(df_merged, "TOTAL")
    resultados = modelo.entrenar_todos()

    print("RESULTADOS")
    for nombre, mse in resultados.items(): # Recorre los resultados
        print(f"{nombre}: {mse}") # muestra el nombre del modelo y su valor

    print("\nPrueba completada")

if __name__ == "__main__":
    main()

#----------------------------------------------------------------------------------------------------------------------#
# Clase: Visualizador
 #mapa_paises
ruta_mapa = r"C:\Proyecto_final_Programacion2\ProyectoFinal_PrograII_SMEK\data\processed\Coordenadas_Paises.csv"
viz_mapa=visualizador(ruta_mapa)
viz_mapa.mapa_paises()
#tendencia total
ruta_mapa2 = r"C:\Proyecto_final_Programacion2\ProyectoFinal_PrograII_SMEK\data\processed\turismo_anios_clean.csv"
viz_mapa_02 = visualizador(ruta_mapa2)
viz_mapa_02.grafico_tendencia_total()

#heatmap_paises
ruta_mapa3= r"C:\Proyecto_final_Programacion2\ProyectoFinal_PrograII_SMEK\data\processed\turismo_anios_clean.csv"
viz_mapa_03 = visualizador(ruta_mapa3)
viz_mapa_03.heatmap_paises()

#grafico de barras
ruta = r"C:\Proyecto_final_Programacion2\ProyectoFinal_PrograII_SMEK\data\processed\zonas_aereas_clean.csv"
viz = visualizador(ruta)
viz.generar_barras_automaticas()
