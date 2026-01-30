import streamlit as st

# Хуудасны зохиомж
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Техникийн төлөв: CAT 793D")
    # Энд шар машины зураг байрлана
    st.image("https://example.com/yellow_truck.png", use_container_width=True)

with col2:
    st.subheader("Мэдрэгчийн мэдээлэл")
    st.metric("Дугуйн даралт", "115 PSI", "Хэвийн")
    st.metric("Хөдөлгүүрийн халалт", "102°C", "Анхаар!", delta_color="inverse")
    st.metric("Байршил", "48.15, 106.91", "Захиргааны хэсэг")
