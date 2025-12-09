#Modelo: Entrena y evalúa modelos supervisados (regresión o clasificación).

# Librerías
from sklearn.model_selection import train_test_split   # divide datos
from sklearn.metrics import mean_squared_error         # calcula error
from sklearn.linear_model import LinearRegression      # regresión lineal
from sklearn.neighbors import KNeighborsRegressor      # KNN
from sklearn.ensemble import RandomForestRegressor     # Random Forest
import pandas as pd

# Clase ModeloML
class ModeloML:

    @staticmethod
    def cargar_csv(ruta): # carga archivo
        try:
            df = pd.read_csv(ruta) # lee el archivo
            print(f"CSV cargado: {ruta}")
            return df
        except Exception as e:
            print(f"Error cargando CSV: {e}") # imprime el error
            return None

    def _init_(self, df, columna_objetivo): # constructor
        self.df = df.copy()             # copia del dataframe
        self.columna_objetivo = columna_objetivo  # columna a trabajar

        # Modelos
        self.modelos = {
            "Regresion_Lineal": LinearRegression(),
            "KNN": KNeighborsRegressor(n_neighbors=3),
            "Random_Forest": RandomForestRegressor(n_estimators=100, random_state=42)
        }

# Preparacion de datos

    def preparar_datos(self):
        """Divide los datos en entrenamiento y prueba."""
        X = self.df.drop(columns=[self.columna_objetivo])  # variables de entrada
        y = self.df[self.columna_objetivo]                 # objetivo

        return train_test_split(X, y, test_size=0.2, random_state=42)

    def entrenar_todos(self):
        X_train, X_test, y_train, y_test = self.preparar_datos() # entrena los modelos
        resultados = {}

        for nombre, modelo in self.modelos.items(): #bucle que recorre los modelos para otener los datos a necesitar
            modelo.fit(X_train, y_train)              # entrenamiento
            y_pred = modelo.predict(X_test)           # predicción
            mse = mean_squared_error(y_test, y_pred)  # error
            resultados[nombre] = mse                  # guarda

        return resultados

    def entrenar(self):
    # Modelo de regresion lineal
        X_train, X_test, y_train, y_test = self.preparar_datos()
        modelo = LinearRegression()
        modelo.fit(X_train, y_train)
        y_pred = modelo.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        return modelo, mse
