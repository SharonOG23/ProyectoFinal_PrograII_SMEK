# Entrena y evalúa modelos supervisados (regresión o clasificación).

# Librerías
from sklearn.model_selection import train_test_split        # divide datos
from sklearn.metrics import mean_squared_error              # calcula errores
from sklearn.linear_model import LinearRegression           # modelo regresión lineal
from sklearn.neighbors import KNeighborsRegressor           # modelo KNN
from sklearn.ensemble import RandomForestRegressor          # modelo Random Forest
import pandas as pd

# Clase ModeloML
class ModeloML:

    @staticmethod
    def cargar_csv(ruta): # carga archivo
        try:
            df = pd.read_csv(ruta) # lee el archivo
            print(f"CSV cargado: {ruta}")  # imprime csv cargado
            return df   # retorna la variable df
        except Exception as e: # captura error y lo guarda em "e"
            print(f"Error cargando CSV: {e}") # imprime el error
            return None         # si hay error, imprime un mensaje de que no se realizo satisfactoriamente

    def __init__(self, df, columna_objetivo):           # constructor
        self.df = df.copy()                             # copia del dataframe
        self.columna_objetivo = columna_objetivo         # columna a trabajar

        # Modelos
        self.modelos = {
            "Regresion_Lineal": LinearRegression(),        # crea modelo de regresion lineal
            "KNN": KNeighborsRegressor(n_neighbors=3),        # crea modelo KNN
            "Random_Forest": RandomForestRegressor(n_estimators=100, random_state=42)  # crea modelo Random forest
        }

# Preparacion de datos

    def preparar_datos(self):  #define metodo
        X = self.df.drop(columns=[self.columna_objetivo])         # variables de entrada quita la clumana objetivo
        y = self.df[self.columna_objetivo]                        # columna objetivo, que se va a usar o que queremos predecir

        return train_test_split(X, y, test_size=0.2, random_state=42)        # divide datos em entrenamiento y prueba

    def entrenar_todos(self):       # metodo que entrena todos los modelos
        X_train, X_test, y_train, y_test = self.preparar_datos()      # entrena los modelos
        resultados = {}           # se guarda aca los resultados de los metodos

        for nombre, modelo in self.modelos.items(): #bucle que recorre los modelos para otener los datos a necesitar
            modelo.fit(X_train, y_train)              # entrenamiento con los datos de entrenamiento
            y_pred = modelo.predict(X_test)           # predicción usando los datos de prueba
            mse = mean_squared_error(y_test, y_pred)  # error, hace comparacion de predicciones con las variables
            resultados[nombre] = mse                  # guarda el resultado

        return resultados  # devuelve los resultados de todos los modelos evaluados

    def entrenar(self):
    # Modelo de regresion lineal
        X_train, X_test, y_train, y_test = self.preparar_datos() # llama al metodo prepara_datos
        modelo = LinearRegression()  # crea la instancia del modelo de regresion lineal
        modelo.fit(X_train, y_train) # relacion con las variables
        y_pred = modelo.predict(X_test) # predice valores de y para x
        mse = mean_squared_error(y_test, y_pred) # mide los errores del modelo
        return modelo, mse   # devuelve el modelo entrenado listo y errores de evaluacion
