import streamlit as st
import pandas as pd
import plotly.express as px
import os

# Title of Dashboard
st.set_page_config(page_title="Smart Financial Dashboard", layout="wide")
st.title("📊 Smart Financial Dashboard")

# Sidebar - File Upload
st.sidebar.header("Upload Financial Data")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type=["csv"])

# Load Data
def load_data(file):
    df = pd.read_csv(file)
    return df

if uploaded_file:
    df = load_data(uploaded_file)
    st.sidebar.success("File Uploaded Successfully!")

    # Show Data Preview
    st.subheader("📊 Data Preview")
    st.write(df.head())

    # Summary Statistics
    st.subheader("📈 Summary Statistics")
    st.write(df.describe())

    # Transaction Trend Visualization
    if 'Date' in df.columns and 'Amount' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'])
        fig = px.line(df, x='Date', y='Amount', title="💰 Transaction Trends Over Time")
        st.plotly_chart(fig)

# API Status Placeholder
st.sidebar.subheader("🌐 API Connection Status")
api_status = st.sidebar.radio("API Connection:", ["Not Connected", "Connected"])
if api_status == "Connected":
    st.sidebar.success("✅ API is Connected!")
else:
    st.sidebar.warning("❌ API Not Connected")

# Forecasting Placeholder
st.subheader("📊 Forecasting Results")
st.write("🔍 Forecasting results will be displayed here once implemented.")

st.sidebar.info("Developed by Tanveer Hussain Mohammed | GitHub: [Your GitHub Link]")
