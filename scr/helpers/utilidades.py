#Contiene funciones auxiliares reutilizables para validaciones, formateo, etc.

# importa librerias
import pandas as pd

# Clase utilidades
class Utilidades:

        @staticmethod
        def cargar_csv(ruta):                   # carga archivo
            try:                                 # inicia un bloque para manejar errores
                df = pd.read_csv(ruta)           # lee el csv
                print(f"CSV cargado: {ruta}")     # imprime un mensaje de carga exitosa
                return df                          # devuelve el df cargado
            except Exception as e:                # si hay un error, lo caotura y lo guarda en "e"
                print(f"Error cargando CSV: {e}")     # imprime el error si hay
                return None            # si hay un error muestra none para indicar que no se realizo bien el proceso

        @staticmethod
        def eliminar_duplicados(df):              # elimina los valores duplicados
            return df.drop_duplicates()            # devuelve el df sin duplicados

        @staticmethod
        def rellenar_nulos(df, valor=0):              # metodo para rellenar los valores nulos
            return df.fillna(valor)               # devuelve el df con los valores nulos rellenados
