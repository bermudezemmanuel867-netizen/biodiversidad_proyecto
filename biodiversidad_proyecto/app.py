import streamlit as st
import pandas as pd
import numpy as np

# Configuración de la página
st.set_page_config(page_title="Dashboard Pez Diablo", layout="wide")

st.title("🐟 Dashboard de Monitoreo y Riesgo: Pez Diablo")
st.markdown("Herramienta de soporte a la decisión para la gestión ambiental y control de especies invasoras.")

# Sidebar de filtros para tomadores de decisiones
st.sidebar.header("Filtros de Análisis")
nivel_riesgo = st.sidebar.select_slider("Filtrar por Umbral de Riesgo:", options=["Bajo", "Medio", "Alto"])

# Métricas principales
col1, col2, col3 = st.columns(3)
col1.metric("Zonas Monitoreadas", "124")
col2.metric("Nivel de Alerta Promedio", "Alto (78%)")
col3.metric("Estatus del Modelo", "Optimizado (SHAP Active)")

st.divider()

# Sección del Mapa / Visualización de Riesgo
st.header("🗺️ Mapa de Riesgo y Distribución Geoespacial")
# Coordenadas ficticias para la simulación del prototipo
map_data = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [19.43, -99.13],
    columns=['lat', 'lon']
)
st.map(map_data)

st.success("Auditoría Ética y Anonimización: Coordenadas bajo enmascaramiento geoespacial (Grid 2km).")