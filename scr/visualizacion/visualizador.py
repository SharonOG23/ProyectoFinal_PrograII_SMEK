import pandas as pd
import os
import csv
import matplotlib.pyplot as plt
import seaborn as sns


# Definición clase visualizador
class visualizador:

    # Constructor
    def __init__(self, ruta_archivo):
        self.__ruta_archivo = ruta_archivo
        self.__encabezado = None
        self.__separador = None
        self.__columnas_validas = None
        self.__decimal = None
        self.__df = None

    # Getters
    @property
    def ruta_archivo(self):
        return self.__ruta_archivo

    @property
    def encabezado(self):
        return self.__encabezado

    @property
    def separador(self):
        return self.__separador

    @property
    def columnas_validas(self):
        return self.__columnas_validas

    @property
    def decimal(self):
        return self.__decimal

    @property
    def df(self):
        return self.__df

    # Setters
    @ruta_archivo.setter
    def ruta_archivo(self, ruta_archivo):
        self.__ruta_archivo = ruta_archivo

    @encabezado.setter
    def encabezado(self, encabezado):
        self.__encabezado = encabezado

    @separador.setter
    def separador(self, separador):
        self.__separador = separador

    @columnas_validas.setter
    def columnas_validas(self, columnas_validas):
        self.__columnas_validas = columnas_validas

    @decimal.setter
    def decimal(self, decimal):
        self.__decimal = decimal

    @df.setter
    def df(self, df):
        self.__df = df

    # ---------------------------------------------------------------
    # Método detección archivo
    # ---------------------------------------------------------------
    def deteccion_archivo_clean(self):

        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.__ruta_archivo = os.path.join(base_dir, "..", "..", self.__ruta_archivo)
        self.__ruta_archivo = os.path.normpath(self.__ruta_archivo)

        with open(self.__ruta_archivo, 'r', encoding='utf-8') as f:
            primera_linea = f.readline()

        # Detectar separador
        self.__separador = csv.Sniffer().sniff(primera_linea).delimiter

        # Detectar decimal
        self.__decimal = "," if "," in primera_linea and "." not in primera_linea else "."

    # ---------------------------------------------------------------
    # Método leer archivo
    # ---------------------------------------------------------------
    def leer_archivo_clean(self):
        self.deteccion_archivo_clean()

        with open(self.__ruta_archivo) as f:
            encabezado = f.readline().strip().split(self.separador)
            self.__columnas_validas = [col for col in encabezado if col]

        self.__df = pd.read_csv(
            self.__ruta_archivo,
            sep=self.__separador,
            decimal=self.__decimal,
            usecols=self.__columnas_validas,
            skiprows=1,
            names=self.__columnas_validas
        )

        print("Archivo cargado correctamente.\n")
        print(f"Ruta: {self.ruta_archivo}\n")
        print(self.__df)
        print("------------------------------------------------------------\n")

    # ---------------------------------------------------------------
    # GRÁFICOS
    # ---------------------------------------------------------------

    def mapa_paises(self, df):
        plt.figure(figsize=(10, 6))
        plt.scatter(df["Longitud"], df["Latitud"])

        for i, row in df.iterrows():
            plt.text(row["Longitud"], row["Latitud"], row["Pais"], fontsize=8)

        plt.title("Ubicación geográfica de países de origen")
        plt.xlabel("Longitud")
        plt.ylabel("Latitud")
        plt.grid(True)
        plt.show()

    def grafico_tendencia_total(self, df):
        plt.figure(figsize=(10, 5))
        plt.plot(df["ANINOS"], df["TOTAL"], marker="o")
        plt.title("Tendencia anual del turismo total en Costa Rica")
        plt.xlabel("Año")
        plt.ylabel("Turistas")
        plt.grid(True)
        plt.show()

    def heatmap_paises(self, df):
        df_temp = df.set_index("ANINOS").drop(columns=["TOTAL"])
        plt.figure(figsize=(14, 8))
        sns.heatmap(df_temp, cmap="YlGnBu")
        plt.title("Heatmap de turismo por país y año")
        plt.show()

    def grafico_barras_horizontales(self, columna, titulo="Barras Horizontales por Zona"):
        plt.figure(figsize=(10, 7))
        plt.barh(self.df["IZONAS"], self.df[columna])
        plt.title(titulo)
        plt.xlabel(columna)
        plt.ylabel("Zonas")
        plt.tight_layout()
        plt.show()




