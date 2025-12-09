#Conecta con SQLite, MySQL, PostgreSQL o SQL Server y permite ejecutar consultas

import sqlite3  #Libreria que me permite crear una base datos portable


import sqlite3
import pandas as pd

class BD:
    def __init__(self, db_name="MigracionCr.db"):
        # Inicializa la conexión a la base de datos
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.crear_tabla()

    #---------------------------------------------------------------------------------
    #--------------------Creacion de las tablas BD:MigracionCr.db----------
    def crear_tabla(self):

        # Creacion tabla Pais
        self.cursor.execute("""
        
        CREATE TABLE IF NOT EXISTS Pais(
            IdPais INTEGER PRIMARY KEY AUTOINCREMENT,
            NombrePais NVARCHAR(100) NOT NULL,
            Latitud DECIMAL(9,6),
            Longitud DECIMAL(9,6),
            Nombre_Continente NVARCHAR(100) NOT NULL
        );
        """)

        # Creacion tabla Clima
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Clima(
            Id_Clima INTEGER PRIMARY KEY AUTOINCREMENT,
            temp_max REAL,
            temp_min REAL,
            rain_mm REAL,
            temp_avg REAL,
            year INTEGER,  
            IdPais INTEGER NOT NULL,
            FOREIGN KEY (IdPais) REFERENCES Pais(IdPais)

        );
        """)

        # Creación Tabla MedioIngreso
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS MedioIngreso (
        Id_medio INTEGER PRIMARY KEY AUTOINCREMENT,
        NombreLugar VARCHAR(100) NOT NULL,
        TipoMedio VARCHAR(50)
        
        );
        """)

    # Creación Tabla Registro
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Total_Ingresos_Anuales (
            Id_Registro INTEGER PRIMARY KEY AUTOINCREMENT,
            ANNIOS INTEGER NOT NULL,
            TOTAL INTEGER NOT NULL,
            CANADA INTEGER,
            ESTADOSUNIDOS INTEGER,
            MEXICO INTEGER,
            BELICE INTEGER,
            ELSALVADOR INTEGER,
            GUATEMALA INTEGER,
            HONDURAS INTEGER,
            NICARAGUA INTEGER,
            PANAMA INTEGER,
            AMERICADELSUR INTEGER,
            CARIBE INTEGER,
            EUROPA INTEGER,
            OTRASZONAS INTEGER
        );
        """)
        self.conn.commit()

    #Metodo que determina a cual continente pertece al pais segun las coordenadas
    def determinar_continente(self, lat, lon):
        # Clasifica continente según latitud/longitud
        if lat < -60:
            return "Antártida"
        elif -60 <= lat <= 83 and -170 <= lon <= -30:
            return "América"
        elif 35 <= lat <= 70 and -25 <= lon <= 60:
            return "Europa"
        elif -35 <= lat <= 37 and -20 <= lon <= 50:
            return "África"
        elif 5 <= lat <= 80 and 60 <= lon <= 180:
            return "Asia"
        elif -50 <= lat <= 10 and 110 <= lon <= 180:
            return "Oceanía"
        else:
            return "Desconocido"

    #Metodo para llenar la tabla Pais
    def insertar_paises(self, df: pd.DataFrame):
        # Asegurar que latitud y longitud sean numéricas
        df['Latitud'] = pd.to_numeric(df['Latitud'], errors='coerce')
        df['Longitud'] = pd.to_numeric(df['Longitud'], errors='coerce')

        for _, row in df.iterrows():
            continente = self.determinar_continente(row['Latitud'], row['Longitud'])
            self.cursor.execute("""
                INSERT INTO Pais (NombrePais, Latitud, Longitud, Nombre_Continente)
                VALUES (?, ?, ?, ?)
            """, (row['Pais'], row['Latitud'], row['Longitud'], continente))
        self.conn.commit()

    #Metodo para llenar la tabla Clima
    def insertar_clima(self, df, id_pais: int):

        for row in df.itertuples(index=False):
            self.cursor.execute("""
                INSERT INTO Clima (temp_max, temp_min, rain_mm, temp_avg, year, IdPais)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                row.temp_max,  # accede como atributo
                row.temp_min,
                row.rain_mm,
                row.temp_avg,
                row.year,
                id_pais
            ))
        self.conn.commit()

    # Metodo para insertar medios
    def insertar_medios_ingreso(self):
        registros = [
            ("Aeropuerto Juan Santa Maria", "Aeropuerto"),
            ("Daniel Oduber", "Aeropuerto"),
            ("Tobias Bolaños", "Aeropuerto"),
            ("Limon", "Aeropuerto"),
            ("Terrestre y Fluvial", "Terrestre y Fluvial"),
            ("Maritima", "Maritima")

        ]

        sql = "INSERT INTO MedioIngreso (NombreLugar, TipoMedio) VALUES (?, ?)"
        self.cursor.executemany(sql, registros)
        self.conn.commit()

    #Limpieza CSV turismo_annios_clean.csv
    def limpiar_dataframe_turismo(self,df):
        """
        Elimina columnas específicas y renombra otras en un DataFrame.
        - Elimina: AMARICADELNORTE, AMARICACENTRAL
        - Renombra: MAXICO -> MEXICO, AMARICADELSUR -> AMERICA DEL SUR
        """
        # 1. Eliminar columnas no deseadas
        columnas_a_eliminar = ["AMARICADELNORTE", "AMARICACENTRAL"]
        df = df.drop(columns=columnas_a_eliminar, errors="ignore")

        # 2. Renombrar columnas
        columnas_a_renombrar = {
            "MAXICO": "MEXICO",
            "AMARICADELSUR": "AMERICADELSUR"
        }
        df = df.rename(columns=columnas_a_renombrar)
        return df

    def insertar_total_ingresos_anuales(self, df: pd.DataFrame):
        """
        Inserta los registros de un DataFrame en la tabla Total_Ingresos_Anuales.
        El DataFrame debe tener las columnas con los mismos nombres que la tabla.
        """
        df.to_sql("Total_Ingresos_Anuales", self.conn, if_exists="append", index=False)
        print("✅ DataFrame insertado correctamente en la tabla Total_Ingresos_Anuales.")
        self.conn.commit()

    #Metodo para poder realizar consultas a las tablas
    def consultar_tabla(self, nombre_tabla: str):

        query = f"SELECT * FROM {nombre_tabla}"
        df = pd.read_sql_query(query, self.conn)
        return df


    #Metodo para cerrar la conexion de la Base datos
    def cerrar(self):
        # Cierra la conexión
        self.conn.close()



"""Script de Pruebas
pruebas=BD()
pruebas.crear_tabla()

#Tabla Pais
tabla_pais=pruebas.consultar_tabla("Pais")
print(tabla_pais.head())

#Tabla Clima
tabla_clima=pruebas.consultar_tabla("Clima")
print(tabla_clima.head())

#Tabla MedioIngreso
tabla_MedioIngreso=pruebas.consultar_tabla("MedioIngreso")
print(tabla_MedioIngreso.head())

#Tabla Registro
tabla_Registro=pruebas.consultar_tabla("Registro")
print(tabla_Registro.head())
"""


