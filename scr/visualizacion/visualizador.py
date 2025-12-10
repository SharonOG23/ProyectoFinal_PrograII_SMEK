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
    #este grafico se genera apartir del archivo Coordenadas_Pises.csv
    def mapa_paises(self):
        df = pd.read_csv(self.ruta_archivo)

        plt.figure(figsize=(10, 6))
        plt.scatter(df["Longitud"], df["Latitud"])

        for i, row in df.iterrows():
            plt.text(row["Longitud"], row["Latitud"], row["Pais"], fontsize=8)

        plt.title("Ubicación geográfica de países de origen")
        plt.xlabel("Longitud")
        plt.ylabel("Latitud")
        plt.grid(True)
        plt.show()
    #este grafico se genera apartir de el archivo turismo_anios_clean.csv
    def grafico_tendencia_total(self):
        df = pd.read_csv(self.ruta_archivo)

        plt.figure(figsize=(10, 5))
        plt.plot(df["ANNIOS"], df["TOTAL"], marker="o")
        plt.title("Tendencia anual del turismo total en Costa Rica")
        plt.xlabel("Año")
        plt.ylabel("Turistas")
        plt.grid(True)
        plt.show()

    def heatmap_paises(self):
        df = pd.read_csv(self.ruta_archivo)

        # LIMPIEZA: eliminar espacios dentro de números
        df = df.replace({',': '', ' ': ''}, regex=True)

        # Convertir todo excepto ANINOS y TOTAL a numérico
        for col in df.columns:
            if col not in ["ANNIOS", "TOTAL"]:
                df[col] = pd.to_numeric(df[col], errors="coerce")

        df_temp = df.set_index("ANNIOS").drop(columns=["TOTAL"])

        plt.figure(figsize=(14, 8))
        sns.heatmap(df_temp, cmap="YlGnBu")
        plt.title("Heatmap de turismo por país y año")
        plt.show()

    def generar_barras_automaticas(self):
        import matplotlib.pyplot as plt
        import pandas as pd

        # Cargar CSV
        df = pd.read_csv(self.ruta_archivo)

        # Detectar columnas numéricas excepto IZONAS
        columnas_numericas = [
            col for col in df.columns
            if col != "IZONAS" and pd.api.types.is_numeric_dtype(df[col])
        ]

        # Generar un gráfico por cada columna
        for col in columnas_numericas:
            plt.figure(figsize=(10, 7))
            plt.barh(df["IZONAS"], df[col])
            plt.title(f"Llegadas por zona - {col}")
            plt.xlabel(col)
            plt.ylabel("Zonas")
            plt.tight_layout()
            plt.show()

 #Scrip de prueba de graficos
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

