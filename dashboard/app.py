# DASHBOARD STREAMLIT
import streamlit as st
import pandas as pd
import os
import sys

# ===== Agregar ruta del proyecto =====
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

from scr.visualizacion.visualizador import visualizador
from streamlit_folium import st_folium

# ===== Rutas de tus CSV =====
RUTA_COORDENADAS = os.path.join(BASE_DIR, "data", "processed", "Coordenadas_Paises.csv")
RUTA_TENDENCIA   = os.path.join(BASE_DIR, "data", "processed", "turismo_anios_clean.csv")
RUTA_HEATMAP     = os.path.join(BASE_DIR, "data", "processed", "turismo_anios_clean.csv")
RUTA_BARRAS      = os.path.join(BASE_DIR, "data", "processed", "zonas_aereas_clean.csv")

# ===== Dashboard =====
st.title("Dashboard de Turismo en Costa Rica")
st.sidebar.title("Menú de visualizaciones")

opcion = st.sidebar.selectbox(
    "Selecciona un gráfico",
    [
        "Mapa de Países",
        "Tendencia Total del Turismo",
        "Heatmap por País y Año",
        "Barras Horizontales por Zona (Automático)"
    ]
)

# ================================
# MAPA DE PAÍSES (INTERACTIVO)
# ================================
if opcion == "Mapa de Países":
    st.subheader(" Ubicación geográfica de países visitantes")

    viz = visualizador(RUTA_COORDENADAS)
    mapa = viz.mapa_paises()  # Folium map

    # Mostrar en Streamlit
    st_folium(mapa, width=900, height=600)

# ================================
# TENDENCIA TOTAL
# ================================
elif opcion == "Tendencia Total del Turismo":
    st.subheader(" Tendencia anual del turismo total")

    viz = visualizador(RUTA_TENDENCIA)
    st.pyplot(viz.grafico_tendencia_total())

# ================================
# HEATMAP POR PAÍS
# ================================
elif opcion == "Heatmap por País y Año":
    st.subheader(" Heatmap de turismo por país y año")

    viz = visualizador(RUTA_HEATMAP)
    st.pyplot(viz.heatmap_paises())

# ================================
# BARRAS AUTOMÁTICAS POR ZONA
# ================================
# ================================
# BARRAS AUTOMÁTICAS POR ZONA
# ================================
elif opcion == "Barras Horizontales por Zona (Automático)":
    st.subheader("Llegadas por zona aérea (todos los gráficos)")

    viz = visualizador(RUTA_BARRAS)

    figuras = viz.generar_barras_automaticas()

    # Mostrar una debajo de otra
    for fig in figuras:
        st.pyplot(fig)
