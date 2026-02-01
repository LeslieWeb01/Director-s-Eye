import streamlit as st

# 1. Системийн үндсэн тохиргоо
st.set_page_config(page_title="Rio Tinto | HSE Smart Control", layout="wide")

# 2. Корпорацийн дизайн (Рио Тинто болон Глобал Захирлын хэв маяг)
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .executive-card {
        background-color: #f8fafc;
        border-left: 5px solid #e11d48;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar - Стратегийн төслийн удирдлага
with st.sidebar:
    st.markdown("### 📊 Стратегийн удирдлага")
    project = st.selectbox("Хяналтын горим:", ["Рио Тинто | Үйл ажиллагааны эрсдэл", "ESG ба Нийгмийн хариуцлага", "Санхүүгийн тогтвортой өсөлт"])
    st.divider()
    st.info("IELTS зорилтот оноо: 7.5+") # [cite: 2026-01-29]
    st.caption("Global Director Development Program 2027")

# 4. Төслийн гарчиг
st.title("Уурхайн аюулгүй байдлын ухаалаг хяналтын систем")
st.write("Зорилго: Технологийн хүчээр эрсдэлийг тэглэх, аюулгүй байдлын удирдлагыг шинэ шатанд гаргах")

# 5. Системийн үндсэн ажиллагаа (Data Dashboard)
col1, col2 = st.columns([1.5, 2.5])

with col1:
    st.markdown('<div class="executive-card">', unsafe_allow_html=True)
    st.subheader("Дижитал ихэр & Мэдрэгчийн хяналт")
    try:
        st.image("upscalemedia-transformed.jpg", caption="CAT 793D | Секунд тутмын бүртгэл", use_container_width=True)
    except:
        st.error("Системийн мэдэгдэл: Техникийн дүрслэл ачааллахад алдаа гарлаа.")
    
    st.write("**Чичиргээ:** Хэвийн")
    st.write("**Температур:** 92°C")
    st.write("**Агаарын чанар:** 98%")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.subheader("AI Аналитик & Урьдчилан таамаглал")
    
    # KPI үзүүлэлтүүд
    k1, k2, k3 = st.columns(3)
    k1.metric("Эрсдэлийн магадлал", "0.01%", "-0.05%")
    k2.metric("Хөрөнгө оруулагчийн итгэл", "96%", "+2%")
    k3.metric("Хувьцааны тогтворжилт", "Тэргүүлэх", "Зорилтот")

    st.divider()
    
    # Таны ирүүлсэн логик: 1 цагийн доторх эрсдэлийг тооцоолох
    st.subheader("AI Таамаглал (Ирэх 1 цаг)")
    st.warning("Мэдэгдэл: Дараагийн 1 цагийн дотор гаж үзэгдэл илрэх магадлал бага байна. Систем автомат хяналтад байна.")
    
    st.text_area("Системийн тайлан (Секундэд бэлтгэв)", 
                 value="Эрсдэл тэглэгдсэн. Гэнэтийн осол болон үйл ажиллагааны зогсолтоос урьдчилан сэргийлэх алгоритм идэвхтэй. Удирдлагын баг стратегийн шийдвэр гаргахад бэлэн.", 
                 height=100)

st.caption("Strategic Data Fusion | Developed for Future Global Director Excellence [cite: 2026-01-29]")
