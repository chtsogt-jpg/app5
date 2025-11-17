import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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
    ["Line Plot", "Bar Chart", "Scatter Plot", "Histogram"]
)

# Number of data points
num_points = st.sidebar.slider("Number of Data Points:", 10, 100, 30)

# Data pattern
pattern = st.sidebar.radio(
    "Data Pattern:",
    ["Random", "Linear", "Exponential"]
)

# Custom title
title = st.sidebar.text_input("Chart Title:", "My Chart")

# Generate data
np.random.seed(42)

if pattern == "Random":
    x = np.arange(num_points)
    y = np.random.randn(num_points) * 10 + 50
elif pattern == "Linear":
    x = np.arange(num_points)
    y = x * 2 + np.random.randn(num_points) * 5
else:  # Exponential
    x = np.arange(num_points)
    y = np.exp(x / 10) + np.random.randn(num_points) * 2

# Create dataframe
df = pd.DataFrame({'X': x, 'Y': y})

# Display statistics
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Mean", f"{df['Y'].mean():.2f}")
with col2:
    st.metric("Max", f"{df['Y'].max():.2f}")
with col3:
    st.metric("Min", f"{df['Y'].min():.2f}")

# Create visualization
fig, ax = plt.subplots(figsize=(10, 6))

if chart_type == "Line Plot":
    ax.plot(df['X'], df['Y'], marker='o', linewidth=2, markersize=5)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    
elif chart_type == "Bar Chart":
    ax.bar(df['X'], df['Y'], color='steelblue')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    
elif chart_type == "Scatter Plot":
    ax.scatter(df['X'], df['Y'], s=100, alpha=0.6, c=df['Y'], cmap='viridis')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    
else:  # Histogram
    ax.hist(df['Y'], bins=20, color='coral', edgecolor='black')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')

ax.set_title(title, fontsize=16, fontweight='bold')
ax.grid(True, alpha=0.3)

st.pyplot(fig)

# Show data table
st.subheader("Data Table")
st.dataframe(df)

# Download button
csv = df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="Download Data as CSV",
    data=csv,
    file_name='data.csv',
    mime='text/csv'
)