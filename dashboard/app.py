#DASHBOARD
import sys
import os
import streamlit as st
import pandas as pd

# ===== Agregar ruta del proyecto =====
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

from scr.visualizacion.visualizador import visualizador

# ===== Dashboard =====
st.title(" Dashboard de Turismo")

file = st.sidebar.file_uploader("Cargar CSV", type=["csv"])

if file:
    df = pd.read_csv(file)
    st.success("CSV cargado correctamente")

    vis = visualizador(df)

    opcion = st.sidebar.selectbox(
        "Selecciona un gráfico",
        ["Mapa de Países", "Tendencia Total", "Heatmap por País", "Barras Horizontales"]
    )

    if opcion == "Mapa de Países":
        st.pyplot(vis.mapa_paises(df))

    elif opcion == "Tendencia Total":
        st.pyplot(vis.grafico_tendencia_total(df))

    elif opcion == "Heatmap por País":
        st.pyplot(vis.heatmap_paises(df))

    elif opcion == "Barras Horizontales":
        col = st.sidebar.selectbox("Columna", df.columns)
        st.pyplot(vis.grafico_barras_horizontales(col))

else:
    st.info("Sube un archivo CSV para comenzar.")