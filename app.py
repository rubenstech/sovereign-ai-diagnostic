import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Diagnóstico de Soberanía C-Level | SmartWorld AI",
    page_icon="🛡️",
    layout="centered"
)

# Estilos CSS optimizados para forzar el fondo oscuro y corregir la visibilidad
st.markdown("""
    <style>
    /* Forzar fondo oscuro en todo el contenedor principal de Streamlit */
    [data-testid="stAppViewContainer"] {
        background-color: #0F172A;
        color: #F8FAFC;
    }
    [data-testid="stHeader"] {
        background-color: rgba(0,0,0,0);
    }
    .stButton>button { 
        width: 100%; 
        background-color: #2563EB; 
        color: white; 
        font-weight: bold; 
        border-radius: 8px; 
        padding: 12px; 
    }
    .stButton>button:hover { background-color: #1D4ED8; }
    .metric-card { 
        background: #1E293B; 
        padding: 20px; 
        border-radius: 10px; 
        border: 1px solid #334155; 
        margin-bottom: 20px; 
        color: #F8FAFC;
    }
    
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

# Formulario de Diagnóstico
with st.form("diagnostic_form"):
    
    st.markdown("### 1. 🧠 Test de Amnesia Corporativa")
    q1 = st.radio(
        "Si el próximo lunes renuncia su pieza clave de ingeniería, operaciones o procesos, ¿en cuánto tiempo su empresa empieza a perder dinero?",
        [
            "Inmediatamente (El 80% del conocimiento vive en su cabeza).",
            "En pocas semanas (Tenemos manuales dispersos en PDFs obsoletos).",
            "Tenemos procesos documentados, estructurados e inmutables."
        ],
        key="q1"
    )
    
    st.markdown("### 2. 🔐 Test de Riesgo de 'Shadow AI'")
    q2 = st.radio(
        "¿Cómo gestiona actualmente su organización el uso de herramientas de Inteligencia Artificial (ChatGPT, nubes externas) entre sus equipos?",
        [
            "Cada colaborador usa herramientas externas por su cuenta con datos de la empresa.",
            "Usamos cuentas corporativas sueltas, pero sin una directiva de seguridad clara.",
            "Tenemos una infraestructura controlada, soberana y aislada."
        ],
        key="q2"
    )
    
    st.markdown("### 3. ⚙️ Test de Fricción Operativa (ERP / Aduanas)")
    q3 = st.radio(
        "¿Cuánto tiempo y esfuerzo humano invierte su equipo procesando datos no estructurados?",
        [
            "Horas de trabajo manual diario; es nuestro mayor cuello de botella.",
            "Tenemos macros o procesos semiautomáticos que fallan a menudo.",
            "Todo nuestro flujo transaccional está integrado y automatizado nativamente."
        ],
        key="q3"
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    submit_button = st.form_submit_button(label="🚀 Calcular Índice de Exposición C-Level")

# Procesamiento al hacer clic en el botón del formulario
if submit_button:
    score = 0
    
    if "Inmediatamente" in q1: score += 40
    elif "pocas semanas" in q1: score += 20
    else: score += 5
    
    if "Cada colaborador" in q2: score += 35
    elif "cuentas corporativas" in q2: score += 20
    else: score += 5
    
    if "Horas de trabajo" in q3: score += 25
    elif "macros" in q3: score += 15
    else: score += 5

    exposure = min(score, 95)
    
    perdida_amnesia = "$45,000 - $120,000 USD" if exposure > 60 else "$15,000 - $40,000 USD" if exposure > 30 else "$5,000 USD (Riesgo Bajo)"
    costo_friccion = "Alto (Sueldos quemados en tareas manuales repetitivas)" if "Horas de trabajo" in q3 else "Moderado (Ineficiencias intermitentes)" if "macros" in q3 else "Optimizado"

    st.success("¡Diagnóstico procesado con éxito por el motor de SmartWorld AI!")
    
    st.markdown("## 📊 Reporte Preliminar Ejecutivo")
    
    if exposure >= 60:
        st.error(f"🚨 **Nivel de Exposición Crítica: {exposure}% (Riesgo Alto)**")
    elif exposure >= 30:
        st.warning(f"⚠️ **Nivel de Exposición Moderada: {exposure}% (Atención Requerida)**")
    else:
        st.success(f"✅ **Nivel de Exposición Controlada: {exposure}% (Estructura Estable)**")

    st.markdown(f"""
    <div class='metric-card'>
    <ul>
        <li><b>Impacto Estimado por Amnesia Corporativa:</b> Pérdida potencial anualizada valorada en <b>{perdida_amnesia}</b> por dependencia de talento crítico.</li>
        <li><b>Vulnerabilidad de Datos (Shadow AI):</b> Exposición activa de flujos e información sensible ante plataformas de terceros sin gobernanza.</li>
        <li><b>Fricción Operativa (ERP/Logística):</b> Nivel detectado: <b>{costo_friccion}</b>.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 💎 Desbloquea el Resumen Ejecutivo & Plan de Blindaje (Living BlueBook)")
    
    st.info("""
    Este **Resumen Express** muestra la superficie del problema. El **Resumen Ejecutivo Completo (Living BlueBook en PDF)** incluye:
    1. La auditoría matemática exacta de sus fugas financieras y costos de ineficiencia ocultos.
    2. La arquitectura personalizada de **Blindaje Patrimonial (Brainness Corp)** para asegurar su propiedad intelectual.
    3. La hoja de ruta de despliegue del **AI Pain-Matching Engine (EurekAI On-Demand™)** adaptada a su ERP / operaciones.
    """)
    
    st.markdown("""
    <div style='text-align: center; margin-top: 25px;'>
        <a href='https://buy.stripe.com/tu-enlace-de-pago' target='_blank' style='background-color: #2563EB; color: white; padding: 15px 30px; text-decoration: none; font-weight: bold; border-radius: 8px; font-size: 16px; box-shadow: 0 4px 12px rgba(37,99,235,0.4);'>
            💳 Adquirir Resumen Ejecutivo y Agendar Sesión C-Level ($150 USD)
        </a>
    </div>
    """, unsafe_allow_html=True)
