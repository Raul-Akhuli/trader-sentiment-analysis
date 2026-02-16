import streamlit as st
import pandas as pd

st.title("Trader Behavior vs Market Sentiment Dashboard")

data = pd.read_csv("csv_files/cleaned_trader_data.csv")

chart_data = data[['date', 'daily_pnl']].copy()
chart_data['date'] = pd.to_datetime(chart_data['date'])
chart_data = chart_data.set_index('date')

st.line_chart(chart_data)
