import streamlit as st

# 1. Enterprise Level Configuration
st.set_page_config(
    page_title="Director's Eye | Operational Intelligence",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Modern UI Styling (No Emojis, Minimalist)
st.markdown("""
    <style>
    .stApp { background-color: #f4f7f9; }
    .main-header { font-size: 24px; font-weight: 600; color: #1e293b; margin-bottom: 20px; }
    .data-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 8px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar Navigation (Professional Menu)
with st.sidebar:
    st.markdown("### Executive Navigation")
    st.radio("Dashboard View", ["Fleet Overview", "HSE Analytics", "Risk Assessment", "ESG Reporting"])
    st.divider()
    st.caption("Strategic Tool for Global Director Excellence")

# 4. Main Dashboard Header
st.markdown('<p class="main-header">Strategic HSE Control Center: Rocanville Operations</p>', unsafe_allow_html=True)

# 5. Core Interface Layout
left_panel, right_panel = st.columns([1.5, 2.5])

with left_panel:
    st.markdown('<div class="data-card">', unsafe_allow_html=True)
    st.subheader("Asset Digital Twin: Unit 7192")
    
    # Visualization Logic
    try:
        st.image("upscalemedia-transformed.jpg", caption="CAT 793D Telemetry Mapping", use_container_width=True)
    except Exception:
        st.error("System Notice: Technical visualization asset currently unavailable in root directory.")
    
    st.metric("Engine Health Status", "98.4%", "Stable")
    st.markdown('</div>', unsafe_allow_html=True)

with right_panel:
    # Key Performance Indicators (KPIs)
    st.subheader("Operational Metrics")
    kpi1, kpi2, kpi3 = st.columns(3)
    kpi1.metric("Mined (MT)", "49,976", "Plan: 75,000")
    kpi2.metric("Engagement Score", "318", "Normal")
    kpi3.metric("Loading Efficiency", "65%", "-5%")

    st.divider()

    # Predictive Intelligence Section
    st.subheader("Actionable Diagnostics")
    
    diagnostics_log = (
        "Analysis: Predictive AI has identified a potential hydraulic variance in the Rear Left Cylinder. "
        "Intervention is recommended within 48 operating hours to maintain operational excellence."
    )
    st.text_area("System Log Output", value=diagnostics_log, height=120)
    
    # ESG and Strategic Alignment
    st.info("Strategic Alignment: Current operations are 100% compliant with Regional HSE and ESG sustainability standards.")

st.caption("Director's Eye v2.0 | Integrated Safety Tech Platform")
