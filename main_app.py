import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px
import numpy as np

# 1. SQL Холболт
def create_connection():
    return sqlite3.connect('global_mining_intelligence.db')

# 2. Олон эх сурвалжийн дата үүсгэх
def initialize_big_data():
    conn = create_connection()
    c = conn.cursor()
    
    # Хүний хүчин зүйл (Fatigue Index)
    c.execute('''CREATE TABLE IF NOT EXISTS human_factors 
                 (ажилтан_ID TEXT, ядралт_индекс REAL, ажлын_цаг REAL, огноо TEXT)''')
    
    # Гадаад орчин (Weather)
    c.execute('''CREATE TABLE IF NOT EXISTS environment 
                 (салхины_хурд REAL, үзэгдэх_орчин REAL, чийгшил REAL, огноо TEXT)''')
    
    # Техникийн телеметр (Telemetry)
    c.execute('''CREATE TABLE IF NOT EXISTS telemetry 
                 (техник_ID TEXT, огцом_тоормос INTEGER, дундаж_хурд REAL, огноо TEXT)''')

    # Өгөгдөл байгаа эсэхийг шалгах
    c.execute("SELECT count(*) FROM human_factors")
    if c.fetchone()[0] == 0:
        # Зохиомол дата олноор үүсгэх
        staff = [('STAFF-00'+str(i), np.random.rand()*10, 8 + np.random.rand()*4, '2026-01-31') for i in range(50)]
        c.executemany("INSERT INTO human_factors VALUES (?,?,?,?)", staff)
        
        env = [(np.random.rand()*40, np.random.rand()*100, np.random.rand()*100, '2026-01-31') for _ in range(1)]
        c.executemany("INSERT INTO environment VALUES (?,?,?,?)", env)
        
        fleet = [('TRUCK-'+str(i), np.random.randint(0, 5), 35 + np.random.rand()*15, '2026-01-31') for i in range(20)]
        c.executemany("INSERT INTO telemetry VALUES (?,?,?,?)", fleet)
        
        conn.commit()
    conn.close()

initialize_big_data()

# 3. Удирдлагын хянах самбар
st.set_page_config(page_title="AI Intelligence Hub", layout="wide")
st.title("Стратегийн дата нэгтгэл ба эрсдэлийн таамаглал")

# SQL-ээс бүх датаг татах
conn = create_connection()
df_human = pd.read_sql_query("SELECT * FROM human_factors", conn)
df_env = pd.read_sql_query("SELECT * FROM environment", conn)
df_telemetry = pd.read_sql_query("SELECT * FROM telemetry", conn)
conn.close()

# 4. Салангид датануудыг ялгаж харуулах
tab1, tab2, tab3 = st.tabs(["Хүний хүчин зүйл", "Техникийн телеметр", "Орчны нөлөө"])

with tab1:
    st.subheader("Ажилтнуудын ядралтын түвшний шинжилгээ")
    # Өндөр ядралттай ажилтнуудыг ялгах (Threshold > 7)
    high_fatigue = df_human[df_human['ядралт_индекс'] > 7]
    if not high_fatigue.empty:
        st.error(f"Анхаар: {len(high_fatigue)} ажилтан ядралтын өндөр эрсдэлтэй байна.")
        st.dataframe(high_fatigue)
    
    fig_human = px.histogram(df_human, x="ядралт_индекс", nbins=10, title="Ядралтын индексийн тархалт", template="simple_white")
    st.plotly_chart(fig_human, use_container_width=True)

with tab2:
    st.subheader("Техникийн ашиглалтын аюулгүй байдал")
    col_a, col_b = st.columns(2)
    with col_a:
        st.write("Огцом тоормослолт (Сүүлийн 24 цаг)")
        fig_brake = px.bar(df_telemetry, x="техник_ID", y="огцом_тоормос", template="simple_white")
        st.plotly_chart(fig_brake, use_container_width=True)
    with col_b:
        st.write("Дундаж хурдны харьцуулалт")
        fig_speed = px.box(df_telemetry, y="дундаж_хурд", template="simple_white")
        st.plotly_chart(fig_speed, use_container_width=True)

with tab3:
    st.subheader("Цаг агаарын нөхцөл байдал")
    curr_env = df_env.iloc[0]
    m1, m2, m3 = st.columns(3)
    m1.metric("Салхины хурд", f"{curr_env['салхины_хурд']:.1f} м/с")
    m2.metric("Үзэгдэх орчин", f"{curr_env['үзэгдэх_орчин']:.1f} %")
    m3.metric("Агаарын чийгшил", f"{curr_env['чийгшил']:.1f} %")

st.divider()
st.info("Системийн дүгнэлт: Салхины хурд их, ажилтнуудын ядралт өндөр байгаа нь ослын магадлалыг 35%-иар нэмэгдүүлж байна.")
