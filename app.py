import streamlit as st
import pandas as pd
import numpy as np

# Set page config
st.set_page_config(page_title="Simple Data Visualizer", page_icon="📊")

# Title
st.title("📊 Simple Data Visualizer")
st.write("Create visualizations with your custom inputs!")

# Sidebar inputs
st.sidebar.header("Settings")

# Chart type selection
chart_type = st.sidebar.selectbox(
    "Choose Chart Type:",
    ["Line Chart", "Bar Chart", "Area Chart"]
)

# Number of data points
num_points = st.sidebar.slider("Number of Data Points:", 10, 100, 30)

# Data pattern
pattern = st.sidebar.radio(
    "Data Pattern:",
    ["Random", "Linear", "Sine Wave"]
)

# Custom title
title = st.sidebar.text_input("Chart Title:", "My Chart")

# Color selection
color = st.sidebar.color_picker("Choose Color:", "#1f77b4")

# Generate data
np.random.seed(42)

if pattern == "Random":
    x = np.arange(num_points)
    y = np.random.randn(num_points).cumsum() + 50
elif pattern == "Linear":
    x = np.arange(num_points)
    y = x * 2 + np.random.randn(num_points) * 5
else:  # Sine Wave
    x = np.arange(num_points)
    y = 10 * np.sin(x / 5) + 50 + np.random.randn(num_points) * 2

# Create dataframe
df = pd.DataFrame({'X': x, 'Y': y})

# Display statistics
st.subheader("📈 Statistics")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Mean", f"{df['Y'].mean():.2f}")
with col2:
    st.metric("Max", f"{df['Y'].max():.2f}")
with col3:
    st.metric("Min", f"{df['Y'].min():.2f}")
with col4:
    st.metric("Std Dev", f"{df['Y'].std():.2f}")

# Display title
st.subheader(title)

# Create visualization based on user selection
if chart_type == "Line Chart":
    st.line_chart(df.set_index('X')['Y'], color=color)
    
elif chart_type == "Bar Chart":
    st.bar_chart(df.set_index('X')['Y'], color=color)
    
else:  # Area Chart
    st.area_chart(df.set_index('X')['Y'], color=color)

# Show data table
with st.expander("📋 View Data Table"):
    st.dataframe(df, use_container_width=True)

# Download button
st.sidebar.markdown("---")
st.sidebar.subheader("💾 Export Data")
csv = df.to_csv(index=False).encode('utf-8')
st.sidebar.download_button(
    label="Download CSV",
    data=csv,
    file_name='visualization_data.csv',
    mime='text/csv'
)

# Footer
st.sidebar.markdown("---")
st.sidebar.info("Built with Streamlit 🎈")
