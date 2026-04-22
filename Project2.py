import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Setup Page Configuration
st.set_page_config(page_title="NSE Kenya Dashboard", layout="wide")

st.title("🇰🇪 Nairobi Securities Exchange (NSE) Analytics")
st.markdown("Monitor performance and trends of Kenyan stocks.")

# 2. Load Data (Replace with your actual NSE data source)
@st.cache_data
def load_data():
    # Example: df = pd.read_csv("nse_data.csv")
    data = {
        'Date': pd.date_range(start='2026-01-01', periods=10, freq='D'),
        'Ticker': ['SCOM', 'KCB', 'EQTY', 'SCOM', 'KCB', 'EQTY', 'SCOM', 'KCB', 'EQTY', 'SCOM'],
        'Price': [55.2, 30.1, 45.5, 56.0, 29.8, 46.2, 54.8, 30.5, 47.0, 55.5],
        'Volume': [1000, 500, 700, 1200, 450, 800, 1100, 600, 750, 1300]
    }
    return pd.DataFrame(data)

df = load_data()

# 3. Sidebar Filters
st.sidebar.header("Filter Options")
ticker_list = df['Ticker'].unique()
selected_ticker = st.sidebar.multiselect("Select Stock(s)", ticker_list, default=ticker_list)

date_range = st.sidebar.date_input("Select Date Range", [])

# 4. Filter the Data
filtered_df = df[df['Ticker'].isin(selected_ticker)]

# 5. Visualizations
col1, col2 = st.columns(2)

with col1:
    st.subheader("Price Trends")
    fig_price = px.line(filtered_df, x='Date', y='Price', color='Ticker', markers=True)
    st.plotly_chart(fig_price, use_container_width=True)

with col2:
    st.subheader("Trading Volume")
    fig_vol = px.bar(filtered_df, x='Date', y='Volume', color='Ticker', barmode='group')
    st.plotly_chart(fig_vol, use_container_width=True)

# 6. Data Table
st.subheader("Raw Market Data")
st.dataframe(filtered_df, use_container_width=True)