import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 1. Хуудасны үндсэн тохиргоо
st.set_page_config(page_title="Уул уурхайн нэгдсэн удирдлагын систем", layout="wide")

# 2. Корпорацийн хэв маяг (Эможигүй, цэвэрхэн загвар)
st.markdown("""
    <style>
    .main { background-color: #f8fafc; }
    [data-testid="stMetricValue"] { color: #0f172a; font-weight: 700; }
    .stPlotlyChart { background-color: #ffffff; border-radius: 8px; border: 1px solid #e2e8f0; }
    h1, h3 { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; color: #1e293b; }
    </style>
    """, unsafe_allow_html=True)

# 3. Өгөгдлийн сан (Мэргэжлийн нэршил)
@st.cache_data
def get_executive_data():
    return pd.DataFrame({
        'Төхөөрөмж': ['CAT 797F Өөрөө буулгагч', 'Komatsu PC8000 Экскаватор', 'P&H 4100XPC Цахилгаан экскаватор', 'Бутлан ангилах хэсэг', 'Туузан дамжуулагч'],
        'Төлөв': ['Ашиглалттай', 'Засвар үйлчилгээтэй', 'Ашиглалттай', 'Ашиглалттай', 'Саатсан'],
        'Ашиглалтын_коэффициент': [95.2, 0.0, 92.5, 88.7, 0.0],
        'Эрсдэлийн_индекс': [0.12, 0.85, 0.22, 0.41, 0.92],
        'Засварын_зардал': [450, 850, 580, 210, 190] # Мянган ам.доллараар
    })

df = get_executive_data()

# 4. Толгой хэсэг
st.title("Стратегийн удирдлага ба аюулгүй ажиллагааны нэгдсэн төв")
st.write("Глобал үйл ажиллагааны хяналт болон хиймэл оюунд суурилсан эрсдэлийн шинжилгээ")

# 5. Хэсгүүдийн сонголт (Tabs)
tab1, tab2, tab3 = st.tabs(["Үйл ажиллагааны тойм", "Тоног төхөөрөмжийн бүтэц", "Эрсдэлийн шинжилгээ"])

with tab1:
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Нийт аюулгүй байдлын индекс", "94.2%", "↑ 0.4%")
    m2.metric("Тоног төхөөрөмжийн бэлэн байдал", "86.5%", "↓ 1.2%", delta_color="inverse")
    m3.metric("ESG хөрөнгө оруулалт", "$1.75 тэрбум", "Төлөвлөгөөт")
    m4.metric("Эрсдэлийн хэлбэлзэл", "Тогтвортой", delta_color="normal")
    
    st.write("---")
    left, right = st.columns([2, 1])
    with left:
        st.subheader("Салбар нэгжүүдийн ашиглалтын харьцуулсан үзүүлэлт")
        fig = px.bar(df, x='Төхөөрөмж', y='Ашиглалтын_коэффициент', 
                     template="simple_white", color_discrete_sequence=['#1e293b'])
        st.plotly_chart(fig, use_container_width=True)
    with right:
        st.subheader("Шийдвэр гаргах түвшин")
        option = st.selectbox("Шаардлагатай арга хэмжээ", ["Тайлан боловсруулах", "Мэдэгдэл хүргүүлэх", "Засварын төлөвлөгөө шинэчлэх", "Яаралтай зогсолт хийх"])
        if st.button("Шийдвэрийг идэвхжүүлэх"):
            st.info(f"Мэдэгдэл: {option} үйлдэл системд бүртгэгдлээ.")

with tab2:
    st.subheader("Үндсэн техник хэрэгслийн ашиглалтын төлөв")
    cols = st.columns(len(df))
    for i, row in df.iterrows():
        with cols[i]:
            st.write(f"**{row['Төхөөрөмж']}**")
            st.write(f"Төлөв: {row['Төлөв']}")
            st.progress(row['Ашиглалтын_коэффициент'] / 100)

with tab3:
    st.subheader("Эрсдэл болон засвар үйлчилгээний хамаарал")
    fig_risk = px.scatter(df, x="Ашиглалтын_коэффициент", y="Эрсдэлийн_индекс", 
                         size="Засварын_зардал", color="Төхөөрөмж",
                         template="simple_white")
    st.plotly_chart(fig_risk, use_container_width=True)

st.divider()
st.caption("Нууцлалын зэрэг: Дотоод хэрэгцээнд | Мэдээллийн шинэчлэгдсэн огноо: 2026-01-31")
