#Utilidades: Contiene funciones auxiliares reutilizables para validaciones, formateo, etc.

# librerias
import pandas as pd

# Clase utilidades
class Utilidades:

        @staticmethod
        def cargar_csv(ruta):  # carga archivo
            try:
                df = pd.read_csv(ruta)  # lee el csv
                print(f"CSV cargado: {ruta}")
                return df
            except Exception as e:
                print(f"Error cargando CSV: {e}")  # imprime el error si hay
                return None

        @staticmethod
        def eliminar_duplicados(df):  # elimina los valores duplicados
            return df.drop_duplicates()  # devuelve sin duplicados

        @staticmethod
        def rellenar_nulos(df, valor=0):  # rellena los valores nulos
            return df.fillna(valor)
