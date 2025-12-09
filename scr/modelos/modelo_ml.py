#Entrena y evalúa modelos supervisados (regresión o clasificación).

# carga librerias
from sklearn.model_selection import train_test_split # divide los datos
from sklearn.metrics import mean_squared_error # calcula el error
from sklearn.linear_model import LinearRegression # modelo de regresion lineal

# Clase ModeloML

class ModeloML:
    def __init__(self, df, columna_objetivo):
        self.df = df.copy()  #  guarda copia del original
        self.columna_objetivo = columna_objetivo
        self.modelo = LinearRegression() # modelo de regresion lineal

    def preparar_datos(self):
        X = self.df.drop(columns=[self.columna_objetivo])
        y = self.df[self.columna_objetivo]
        return train_test_split(X, y, test_size=0.2, random_state=42) # divide valores

    def entrenar(self):   # entrenamiento
        X_train, X_test, y_train, y_test = self.preparar_datos()
        self.modelo.fit(X_train, y_train)
        y_pred = self.modelo.predict(X_test)    # hace predicciones
        mse = mean_squared_error(y_test, y_pred)
        return self.modelo, mse  # devuelve modelo entrenado