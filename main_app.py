import streamlit as st
import pandas as pd

# 1. Хуудасны тохиргоо
st.set_page_config(page_title="Director's Eye | HSE Tech", layout="wide")

# 2. Apple-ийн цэвэрхэн дизайн (Glassmorphism)
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .stMetric { 
        background-color: #ffffff; 
        padding: 15px; 
        border-radius: 20px; 
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Header - Алсын хараа: Global Director
st.title("👨‍💼 Director's Eye Control Center")
st.subheader("Уул уурхайн техникийн нэгдсэн хяналтын самбар")

# 4. Dashboard Layout
col1, col2 = st.columns([1.5, 2.5])

with col1:
    st.info("📦 Техникийн мэдээлэл")
    st.write("**Улсын дугаар:** 7192 ӨМӨ")
    st.write("**Төрөл:** CAT 793D (Haul Truck)")
    
    # Зургийн алдаанаас сэргийлэх логик
    try:
        st.image("upscalemedia-transformed.jpg", caption="Дижитал Ихэр", use_container_width=True)
    except:
        st.warning("🖼️ Зургийн файл GitHub дээр олдохгүй байна. (Upload хийх шаардлагатай)")

with col2:
    st.success("📊 Бодит цагийн мэдрэгчийн өгөгдөл (Sense)")
    
    m1, m2, m3 = st.columns(3)
    m1.metric("Хөдөлгүүр", "94°C", "Хэвийн")
    m2.metric("Түлш", "840 Л", "-12.5%")
    m3.metric("Дугуй", "114 PSI", "Тогтвортой")
    
    st.divider()
    
    st.error("⚠️ AI Таамаглал & Сэрэмжлүүлэг (Analyze)")
    st.write("* **Predictive AI:** Ойрын 24 цагт гидравлик системд саатал гарах магадлал 15% байна.")
    st.write("* **HSE Alert:** Жолоочийн ядралтын индекс өсөх хандлагатай байна.")

st.caption("Developed by Future Global Director | 2026")
