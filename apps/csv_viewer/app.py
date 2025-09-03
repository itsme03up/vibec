import streamlit as st
import pandas as pd
import numpy as np
import base64

# Page configuration
st.set_page_config(
    page_title="CSV Data Visualizer",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .section-header {
        color: #2c3e50;
        border-bottom: 2px solid #3498db;
        padding-bottom: 0.5rem;
        margin-top: 2rem;
    }
    .stButton>button {
        background-color: #3498db;
        color: white;
        border-radius: 5px;
        border: none;
        padding: 0.5rem 1rem;
    }
    .stButton>button:hover {
        background-color: #2980b9;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.header("⚙️ Settings")
    st.markdown("---")
    st.markdown("**Upload Options:**")
    show_sample = st.checkbox("Show sample data", value=False)
    
    st.markdown("---")
    st.markdown("**Chart Options:**")
    chart_type = st.selectbox("Chart Type", ["Line Chart", "Bar Chart", "Area Chart"])
    
    st.markdown("---")
    st.markdown("**About:**")
    st.markdown("This app visualizes CSV data with interactive charts and statistics.")

# Main content
st.markdown('<h1 class="main-header">📊 CSV Data Visualizer</h1>', unsafe_allow_html=True)

# File upload section
col1, col2 = st.columns([3, 1])
with col1:
    uploaded_file = st.file_uploader("📁 Upload your CSV file", type="csv")
with col2:
    if st.button("📋 Use Sample Data"):
        show_sample = True

# Load data
df = None
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success(f"✅ File '{uploaded_file.name}' loaded successfully!")
elif show_sample:
    df = pd.read_csv("sample.csv")
    st.info("ℹ️ Using sample data")

if df is not None:
    # Data overview
    st.markdown('<h2 class="section-header">📋 Data Overview</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Rows", df.shape[0])
    with col2:
        st.metric("Columns", df.shape[1])
    with col3:
        st.metric("Data Types", len(df.dtypes.unique()))
    
    # Data preview
    st.markdown('<h3 class="section-header">🔍 Data Preview</h3>', unsafe_allow_html=True)
    st.dataframe(df.head(10), use_container_width=True)
    
    # Statistics
    st.markdown('<h3 class="section-header">📈 Statistics</h3>', unsafe_allow_html=True)
    st.dataframe(df.describe(), use_container_width=True)
    
    # Visualization
    st.markdown('<h3 class="section-header">📊 Visualization</h3>', unsafe_allow_html=True)
    
    # Column selection
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    if numeric_cols:
        selected_col = st.selectbox("Select a numeric column to visualize", numeric_cols)
        
        # Chart
        if chart_type == "Line Chart":
            st.line_chart(df[selected_col])
        elif chart_type == "Bar Chart":
            st.bar_chart(df[selected_col])
        elif chart_type == "Area Chart":
            st.area_chart(df[selected_col])
        
        # Additional insights
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Mean", f"{df[selected_col].mean():.2f}")
        with col2:
            st.metric("Median", f"{df[selected_col].median():.2f}")
        with col3:
            st.metric("Std Dev", f"{df[selected_col].std():.2f}")
    else:
        st.warning("⚠️ No numeric columns found for visualization")
    
    # Download processed data
    st.markdown('<h3 class="section-header">💾 Download</h3>', unsafe_allow_html=True)
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="processed_data.csv">📥 Download Processed CSV</a>'
    st.markdown(href, unsafe_allow_html=True)

else:
    st.info("👆 Please upload a CSV file or click 'Use Sample Data' to get started!")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit")
