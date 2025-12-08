# 📊 Análisis y Predicción del Turismo en Costa Rica
### Carrera: Big Data
### Curso: Programación II
### Examen III

[![Carga de datos](https://img.shields.io/badge/Cargar%20datos-CSV-4CAF50?style=for-the-badge&logo=files)]()
[![Limpieza de datos](https://img.shields.io/badge/Limpieza%20y%20EDA-Procesamiento-2196F3?style=for-the-badge&logo=databricks)]()  
[![Visualizaciones](https://img.shields.io/badge/Visualizaciones-Matplotlib-9C27B0?style=for-the-badge&logo=plotly)]()  
[![Modelado supervisado](https://img.shields.io/badge/Modelado-Supervisado-FF9800?style=for-the-badge&logo=mlflow)]()  
[![Documentación](https://img.shields.io/badge/Documentación-Notebook-795548?style=for-the-badge&logo=jupyter)]()  
[![Dashboard](https://img.shields.io/badge/Dashboard-Streamlit-E91E63?style=for-the-badge&logo=streamlit)]()  
[![API](https://img.shields.io/badge/🔌_API-Disponible-blue?style=for-the-badge)]()
---
## 👥 Integrantes del Proyecto.
- **Sharon Obando Gómez**
- **Marco Alvarez Quirós**
- **Eunice Brenes Granados**
- **Kristel Hernández Mena**
---
## 📝 Descripción del Proyecto.
Este repositorio corresponde al tercer examen del curso **Programación II**. El objetivo de nuestro proyecto es:
Incluir un análisis exploratorio y visualizaciones previas al modelado.
Este proyecto busca analizar el comportamiento del turismo en Costa Rica y
predecir la cantidad de visitantes anual o mensual, considerando factores como el
clima, el país de origen de los turistas y eventos relevantes.

El proyecto contiene:

📥 Cargar datos desde archivos CSV.

🧹 Limpiar y procesar la información (EDA).

📊 Generar visualizaciones utilizando matplotlib.

🧱 Modelado Supervisado.

🔌 Consumir datos desde una API.

📓 Documentar y presentar resultados con notebook.

🖥️ Crear un dashboard con Streamlit.

---
## 🗂️ Estructura del Repositorio.
```
proyecto_nombre/
├── src/ # Código fuente principal
│ ├── datos/ # Gestión de archivos y transformación de datos
│ ├── basedatos/ # Módulos para conexión a bases de datos
│ ├── api/ # Clientes para llamadas a APIs externas
│ ├── eda/ # Exploración de datos y estadísticas descriptivas
│ ├── visualizacion/ # Visualización de datos y mapas
│ ├── modelos/ # Entrenamiento y evaluación de modelos ML
│ ├── helpers/ # Funciones auxiliares reutilizables
│ └── main.py # Punto de entrada del proyecto
│
├── notebooks/ # Jupyter notebooks para desarrollo y presentación
│ └── exploracion_inicial.ipynb
│
├── dashboard/ # Dashboard interactivo con Streamlit
│ └── app.py
│
├── data/ # Archivos (CSV, Excel, JSON, etc.)
└── raw #Archivos en crudo
└── processed #Archivos procesados
```

---
## 📦 Librerías Utilizadas.
- pandas
- matplotlib
- streamlit
- Conexión a base de dato: sqlalchemy -> Se importa 'create_engine'
- API's: requests
---

## 🌐 CSV: Instituto Costarricense de Turismo.
```
Link: https://www.ict.go.cr/es/estadisticas/informes-estadisticos.html
```
---

## 🔌 API de Clima: Open-Meteo
```
Link: https://open-meteo.com/
```
---
**Este proyecto es únicamente para fines académicos como parte de nuestro Examen III de Programación - Big Data.**
