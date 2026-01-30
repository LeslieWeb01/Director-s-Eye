import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 1. Page Config
st.set_page_config(page_title="Mining Executive Hub", layout="wide")

# 2. Advanced CSS for Professional UI
st.markdown("""
    <style>
    .main { background-color: #f8fafc; }
    .stMetric { background-color: #ffffff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 20px; }
    .status-active { color: #10b981; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 3. Enhanced Data Engine
@st.cache_data
def get_mining_data():
    return pd.DataFrame({
        'Тоног_төхөөрөмж': ['CAT 797F Truck', 'Komatsu PC8000', 'P&H 4100XPC', 'Crushing Plant', 'Conveyor System'],
        'Төлөв': ['Ажиллаж байна', 'Засвартай', 'Ажиллаж байна', 'Ажиллаж байна', 'Сатсан'],
        'Гүйцэтгэл': [95, 0, 92, 88, 0],
        'Эрсдэл': [0.1, 0.8, 0.2, 0.4, 0.9],
        'Шатахуун_Зарцуулалт': [850, 0, 1200, 450, 150]
    })

df_fleet = get_mining_data()

# 4. Header with Global Identity
st.title("Strategic Mining & HSE Control Hub")
st.write("Глобал уурхайн үйл ажиллагаа болон техник төхөөрөмжийн нэгдсэн удирдлага")

# 5. Global Navigation (Tabs)
tab1, tab2, tab3 = st.tabs(["📊 Ерөнхий хяналт", "🚜 Техник төхөөрөмжийн бүтэц", "⚠️ Эрсдэлийн удирдлага"])

with tab1:
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Нийт ашигт ажиллагаа", "89.4%", "↑ 2.1%")
    m2.metric("Сул зогсолт", "4.2 цаг", "-1.5", delta_color="inverse")
    m3.metric("Хөдөлмөрийн аюулгүй байдал", "100%", "Тогтвортой")
    m4.metric("Байгаль орчны нийцэл (ESG)", "98.1%", "↑ 0.5%")
    
    st.write("---")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader("Салбар нэгжүүдийн гүйцэтгэлийн харьцуулалт")
        fig = px.bar(df_fleet, x='Тоног_төхөөрөмж', y='Гүйцэтгэл', color='Гүйцэтгэл', 
                     color_continuous_scale='Blues', template='plotly_white')
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        st.subheader("Шуурхай шийдвэр гаргалт")
        action = st.selectbox("Үйлдэл сонгох", ["Тайлан татах", "Мэдэгдэл илгээх", "Засвар төлөвлөх", "Яаралтай зогсолт"])
        if st.button("Шийдвэрийг баталгаажуулах"):
            st.warning(f"АНХААР: '{action}' үйлдэл Глобал түвшинд идэвхжлээ.")

with tab2:
    st.subheader("Уурхайн үндсэн техникийн паркийн төлөв")
    # Техник бүрийн мэдээллийг Card хэлбэрээр харуулах
