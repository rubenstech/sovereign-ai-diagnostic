import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Diagnóstico de Soberanía C-Level | SmartWorld AI",
    page_icon="🛡️",
    layout="centered"
)

# Estilos CSS limpios y corporativos con centrado optimizado para el header
st.markdown("""
    <style>
    .main { background-color: #0F172A; color: #F8FAFC; }
    .stButton>button { width: 100%; background-color: #2563EB; color: white; font-weight: bold; border-radius: 8px; padding: 12px; }
    .stButton>button:hover { background-color: #1D4ED8; }
    .metric-card { background: #1E293B; padding: 20px; border-radius: 10px; border: 1px solid #334155; margin-bottom: 20px; }
    
    /* Contenedor del encabezado centrado */
    .header-container {
        text-align: center;
        padding: 20px 10px;
    }
    .header-container h2 {
        color: #FFFFFF;
        font-size: 26px;
        font-weight: 700;
        margin-top: 10px;
        line-height: 1.3;
    }
    .header-container p {
        color: #94A3B8;
        font-size: 15px;
        margin-top: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# Encabezado principal perfectamente centrado
st.markdown("""
    <div class="header-container">
        <div style="font-size: 40px;">🛡️</div>
        <h2>Diagnóstico de Soberanía Cognitiva e Inmunidad Operativa</h2>
        <p>Evalúa el riesgo de Amnesia Corporativa, Shadow AI y Fricción Operativa en tu organización.</p>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")
