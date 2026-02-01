import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Director's Eye | Strategic HSE Intelligence", layout="wide")

# 2. Corporate Design (Clean Minimalist)
st.markdown("""
    <style>
    .reportview-container { background: #fdfdfd; }
    .metric-card {
        background-color: #ffffff;
        border: 1px solid #e1e4e8;
        padding: 20px;
        border-radius: 12px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Executive Header
st.title("Strategic HSE Control Center")
st.write("Current Focus: Predictive Fleet Maintenance and Operational Safety")

# 4. Main Interface Layout
col_twin, col_data = st.columns([1.5, 2.5])

with col_twin:
    st.header("Asset Digital Twin: 7192 OMO")
    
    # Error Handling for Image Asset
    try:
        st.image("upscalemedia-transformed.jpg", 
                 caption="CAT 793D Telemetry Mapping", 
                 use_container_width=True)
    except FileNotFoundError:
        st.error("Status: Visualization Asset Missing. Please upload 'upscalemedia-transformed.jpg' to the GitHub root directory.")

with col_data:
    st.header("Predictive Analytics Stream")
    
    # Core Metrics
    m1, m2, m3 = st.columns(3)
    m1.metric("Engine Health Index", "98.4%", "Stable")
    m2.metric("Fuel Optimization", "1,240 L", "-2.1%")
    m3.metric("Safety Fatigue Score", "0.12", "Normal")

    st.markdown("---")
    
    # Strategic Insights (Vantiq Logic: Sense-Analyze-Act)
    st.subheader("Actionable Intelligence")
    
    st.text_area("System Diagnostics
