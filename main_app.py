import streamlit as st

# 1. Хуудасны үндсэн тохиргоо (Apple + Vantiq Aesthetic)
st.set_page_config(page_title="Mining Intelligence Hub", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #f8fafc; }
    .glass-card {
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(15px);
        border-radius: 24px;
        padding: 25px;
        border: 1px solid rgba(255, 255, 255, 0.3);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.07);
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Header - Сайн байна уу, Захирал аа
st.title("Өглөөний мэнд, Захирал аа")
st.write("Өнөөдөр системд 2 онцгой мэдэгдэл бүртгэгдсэн байна.")

# 3. Main Layout
col1, col2 = st.columns([1.5, 2.5])

with col1:
    # Дижитал ихэр (Digital Twin) хэсэг
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.subheader("Техникийн Дижитал Ихэр: 7192 ӨМӨ")
    # Таны ирүүлсэн CAT ачааны машины зургийг энд байрлуулна
    st.image("upscalemedia-transformed.jpg", use_container_width=True)
    
    st.metric("Хөдөлгүүрийн ажиллагаа", "98.4%", "Тогтвортой")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    # Мэдрэгчийн шинжилгээ (Vantiq Logic)
    st.subheader("Техникийн ерөнхий шинжилгээ")
    
    m_col1, m_col2, m_col3 = st.columns(3)
    with m_col1:
        st.metric("Түлшний түвшин", "1,240 Л", "Хэвийн")
    with m_col2:
        st.metric("Дугуйн даралт", "116 PSI", "+2 PSI")
    with m_col3:
        st.metric("Тосны халалт", "102°C", "Анхаар!", delta_color="inverse")

    st.divider()
    
    # "Schedule" болон "Alerts" хэсэг (Эрүүл мэндийн апп-ын загвараар)
    st.subheader("Төлөвлөгөөт засвар үйлчилгээ")
    st.info("🔧 Дараагийн тос солилт: 48 цагийн дараа (HT-104)")
    st.warning("⚠️ Сэрэмжлүүлэг: Зүүн хойд дугуйн элэгдэл 85%-д хүрсэн байна.")

st.caption("Strategic Data Fusion | AI Orchestrator v2.0")
