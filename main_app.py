import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# 1. Page Configuration
st.set_page_config(page_title="Director's Eye v2", layout="wide", page_icon="👁️")

# 2. Advanced Styling (Corporate Dark Theme)
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    div[data-testid="stMetricValue"] { color: #10b981; font-size: 32px; }
    .stPlotlyChart { border: 1px solid #374151; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar - The Visionary Panel
st.sidebar.image("https://img.icons8.com/fluency/96/shield-with-eye.png")
st.sidebar.title("Strategic HQ")
st.sidebar.info("System: Active | Region: Global")
st.sidebar.write("---")
st.sidebar.write("🎯 **Goal:** 2027 MBA & Global HSE Leadership")
st.sidebar.write("🦾 **Tech:** Python Predictive AI")

# 4. Header Section
st.title("🛡️ DIRECTOR'S EYE: Intelligence Hub")
st.write("Real-time ESG & Safety Analytics for Global Mining Assets")

# 5. Data Engine (BHP / Rio Tinto Simulation)
@st.cache_data
def get_strategic_data():
    data = pd.DataFrame({
        'Asset': ['Pilbara Iron', 'Oyu Tolgoi', 'Escondida', 'Olympic Dam', 'Antamina'],
        'Compliance': [99.2, 97.5, 94.8, 91.2, 88.5],
        'Risk_Index': [0.1, 0.2, 0.4, 0.5, 0.8],
        'AI_Forecast': [0.05, 0.08, 0.15, 0.22, 0.45]
    })
    return data

df = get_strategic_data()

# 6. Executive Metrics (The "Predictive" Core)
m1, m2, m3 = st.columns(3)
with m1:
    st.metric("Global Compliance", f"{df['Compliance'].mean():.1f}%", "↑ 0.8%")
with m2:
    st.metric("Predictive Accuracy", "96.4%", "AI Active")
with m3:
    st.metric("Critical Alerts", "1 Low Risk", "-2", delta_color="inverse")

st.divider()

# 7. Strategic Visuals
col_left, col_right = st.columns(2)

with col_left:
    st.write("### 📊 Site Performance Matrix")
    fig1 = px.bar(df, x='Asset', y='Compliance', color='Risk_Index',
                  color_continuous_scale='RdYlGn_r', template='plotly_dark')
    st.plotly_chart(fig1, use_container_width=True)

with col_right:
    st.write("### 🔮 AI Predictive Risk Forecast")
    fig2 = px.line(df, x='Asset', y='AI_Forecast', markers=True, 
                   line_shape='spline', template='plotly_dark')
    fig2.update_traces(line_color='#ef4444')
    st.plotly_chart(fig2, use_container_width=True)

st.success("✅ Global Data Sync Complete. 'Director's Eye' is monitoring all assets.")
