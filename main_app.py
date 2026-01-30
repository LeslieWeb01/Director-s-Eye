import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 1. Page Config
st.set_page_config(page_title="HSE Global Director Intelligence", layout="wide")

# 2. Executive Theme Styling
st.markdown("""
    <style>
    .main { background-color: #f1f5f9; }
    [data-testid="stMetricValue"] { color: #1e293b; font-weight: 700; }
    .stPlotlyChart { background-color: #ffffff; border-radius: 12px; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1); }
    </style>
    """, unsafe_allow_html=True)

# 3. Data Engine (Enhanced for Sophistication)
@st.cache_data
def get_advanced_data():
    return pd.DataFrame({
        'Asset': ['Pilbara Iron', 'Oyu Tolgoi', 'Escondida', 'Olympic Dam', 'Antamina'],
        'Compliance_Score': [99.2, 97.5, 94.8, 91.2, 88.5],
        'Risk_Level': [1.2, 2.1, 3.5, 4.2, 5.0],
        'Investment_ESG': [450, 320, 580, 210, 190], # in Millions
        'AI_Forecast_Trend': [0.2, -0.5, 1.1, 0.8, 2.3]
    })

df = get_advanced_data()

# 4. Header Section
st.title("Strategic HSE & ESG Intelligence")
st.caption("Operational Decision Support System | 2026 Fiscal Year")

# 5. High-Level Metrics
m1, m2, m3, m4 = st.columns(4)
with m1:
    st.metric("Group Safety Index", "94.2%", "↑ 0.4%")
with m2:
    st.metric("Total Managed Assets", "5 Global Units")
with m3:
    st.metric("ESG Investment", "$1.75B", "FY26 Projected")
with m4:
    st.metric("Risk Variance", "Stable", delta_color="normal")

st.write("---")

# 6. Advanced Visuals (Sophisticated Layout)
col_a, col_b = st.columns([2, 1])

with col_a:
    st.subheader("Asset Performance vs. ESG Investment Matrix")
    # Bubble chart for complex data visualization
    fig1 = px.scatter(df, x="Compliance_Score", y="Risk_Level", 
                     size="Investment_ESG", color="Asset",
                     hover_name="Asset", log_x=False, size_max=60,
                     template="plotly_white", title="Performance Correlation")
    fig1.update_layout(showlegend=False)
    st.plotly_chart(fig1, use_container_width=True)

with col_b:
    st.subheader("Regional Risk Benchmarking")
    # Radar chart for sophisticated comparison
    fig2 = go.Figure(data=go.Scatterpolar(
      r=df['Risk_Level'],
      theta=df['Asset'],
      fill='toself',
      line_color='#1e293b'
    ))
    fig2.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 6])),
                      showlegend=False, height=400)
    st.plotly_chart(fig2, use_container_width=True)

# 7. Predictive Insight Table
st.subheader("AI-Driven Predictive Risk Forecast")
st.table(df[['Asset', 'Compliance_Score', 'AI_Forecast_Trend']].sort_values(by='AI_Forecast_Trend', ascending=False))

st.caption("Strategic Intelligence Division | Internal Use Only")
