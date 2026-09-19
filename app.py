import streamlit as st

# Configuración de la página web estilo C-Level
st.set_page_config(
    page_title="Sovereign AI Readiness | SmartWorld AI",
    page_icon="🛡️",
    layout="centered"
)

# Estilos visuales limpios y ejecutivos
st.markdown("""
    <style>
    .main-title { font-size: 28px; font-weight: 700; color: #1E293B; text-align: center; }
    .subtitle { font-size: 16px; color: #64748B; text-align: center; margin-bottom: 30px; }
    .card { background-color: #F8FAFC; padding: 20px; border-radius: 10px; border-left: 5px solid #2563EB; margin-bottom: 15px; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-title">🛡️ Diagnóstico de Soberanía Cognitiva e Inmunidad Operativa</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Evalúa el riesgo de Amnesia Corporativa y el nivel de exposición de tu organización ante la IA.</p>', unsafe_allow_html=True)

# Formulario del Test (Las 3 Preguntas Clave)
with st.form("diagnostic_form"):
    
    st.markdown("### 1. 🧠 Test de Amnesia Corporativa")
    p1 = st.radio(
        "Si el próximo lunes renuncia su pieza clave de ingeniería, operaciones o procesos, ¿en cuánto tiempo su empresa empieza a perder dinero?",
        [
            "Inmediatamente (El 80% del conocimiento vive en su cabeza).",
            "En pocas semanas (Tenemos manuales dispersos en PDFs obsoletos).",
            "Tenemos procesos documentados, estructurados e inmutables."
        ],
        index=0
    )
    
    st.markdown("### 2. 🔒 Test de Riesgo de 'Shadow AI'")
    p2 = st.radio(
        "¿Cómo gestiona actualmente su organización el uso de herramientas de Inteligencia Artificial (ChatGPT, nubes externas) entre sus equipos?",
        [
            "Cada colaborador usa herramientas externas por su cuenta con datos de la empresa.",
            "Usamos cuentas corporativas sueltas, pero sin una directiva de seguridad clara.",
            "Tenemos una infraestructura controlada, soberana y aislada."
        ],
        index=0
    )
    
    st.markdown("### 3. ⚙️ Test de Fricción Operativa (ERP / Aduanas)", unsafe_allow_html=True)
    p3 = st.radio(
        "¿Cuánto tiempo y esfuerzo humano invierte su equipo procesando datos no estructurados (Packing lists, aduanas, ERP/Odoo)?",
        [
            "Horas de trabajo manual diario; es nuestro mayor cuello de botella.",
            "Tenemos macros o procesos semiautomáticos que fallan a menudo.",
            "Todo nuestro flujo transaccional está integrado y automatizado nativamente."
        ],
        index=0
    )
    
    # Datos de contacto corporativo para liberar el reporte
    st.markdown("---")
    st.markdown("### 📋 Datos Corporativos para el Reporte")
    col1, col2 = st.columns(2)
    with col1:
        company_name = st.text_input("Nombre de la Empresa")
        corporate_email = st.text_input("Correo Corporativo")
    with col2:
        executive_name = st.text_input("Nombre del Directivo")
        cargo = st.selectbox("Cargo", ["CEO / Fundador", "CTO / Director de Tecnología", "COO / Director de Operaciones", "Gerente de Área", "Otro"])

    submitted = st.form_submit_button("🚀 Generar Resumen Express de Riesgo")

# Lógica al enviar el formulario
if submitted:
    if not corporate_email or not company_name:
        st.error("⚠️ Por favor, ingresa el nombre de la empresa y tu correo corporativo para procesar el diagnóstico.")
    else:
        # Cálculo simple de riesgo basado en las respuestas
        risk_score = 0
        if "Inmediatamente" in p1: risk_score += 35
        elif "pocas semanas" in p1: risk_score += 20
        
        if "Cada colaborador" in p2: risk_score += 35
        elif "cuentas corporativas" in p2: risk_score += 20
        
        if "Horas de trabajo" in p3: risk_score += 30
        elif "macros" in p3: risk_score += 15

        st.success("✅ ¡Diagnóstico procesado con éxito por el motor de SmartWorld AI!")
        
        # Resultado del Resumen Express (Gratuito)
        st.markdown(f"### 📊 Reporte Preliminar para: {company_name}")
        
        if risk_score > 50:
            st.error(f"🚨 **Nivel de Exposición Crítica: {risk_score}% (Riesgo Alto)**")
            st.markdown("""
                * **Diagnóstico Brainness (Amnesia Corporativa):** Su organización corre un peligro inminente de pérdida de patrimonio intelectual ante la fuga de talento clave.
                * **Diagnóstico EurekAI (Inmunidad Operativa):** Detectamos vulnerabilidades severas por uso de *Shadow AI* y cuellos de botella transaccionales.
            """)
        else:
            st.warning(f"⚠️ **Nivel de Exposición Moderada: {risk_score}% (Riesgo Latente)**")
            st.markdown("Su empresa cuenta con ciertos controles, pero presenta puntos ciegos importantes en la gobernanza de su Propiedad Intelectual y flujos operativos.")

        # La Oferta High Ticket de Entrada (El Resumen Ejecutivo de Pago)
        st.markdown("---")
        st.markdown("### 💎 Desbloquea el Resumen Ejecutivo & Plan de Blindaje (Living BlueBook)")
        st.info("""
            Este **Resumen Express** es solo la superficie. El **Resumen Ejecutivo Completo (Living BlueBook en PDF)** incluye:
            1. La auditoría matemática exacta de sus fugas financieras.
            2. La arquitectura personalizada de **Blindaje Patrimonial (Brainness Corp)**.
            3. La ruta de despliegue del **AI Pain-Matching Engine (EurekAI On-Demand™)** para su ERP.
        """)
        
        # Botón de pasarela de pago o agendamiento C-Level
        st.markdown(
            """
            <a href="https://calendly.com" target="_blank">
                <button style="background-color:#2563EB; color:white; padding:12px 20px; border:none; border-radius:5px; font-size:16px; font-weight:bold; cursor:pointer; width:100%;">
                    💳 Adquirir Resumen Ejecutivo y Agendar Sesión C-Level ($150 USD)
                </button>
            </a>
            """,
            unsafe_allow_html=True
        )