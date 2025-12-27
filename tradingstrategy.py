import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.graph_objects as go
from datetime import datetime, timedelta

st.set_page_config(layout="wide")
st.title("Trading Strategy Visualization (SMA Crossover)")

# --- Sidebar for User Input ---
st.sidebar.header("Strategy Parameters")
ticker_symbol = st.sidebar.text_input("Enter Stock Ticker", "AAPL").upper()
start_date = st.sidebar.date_input("Start Date", datetime.now() - timedelta(days=365 * 2))
end_date = st.sidebar.date_input("End Date", datetime.now())
short_window = st.sidebar.slider("Short SMA Window", 5, 50, 20)
long_window = st.sidebar.slider("Long SMA Window", 20, 200, 50)

# --- Data Fetching ---
@st.cache_data
def get_stock_data(ticker, start, end):
    try:
        data = yf.download(ticker, start=start, end=end)
        if data.empty:
            st.warning(f"No data returned for {ticker}. Please check the ticker symbol and date range.")
            return None
        return data
    except Exception as e:
        st.error(f"Error fetching data for {ticker}: {e}")
        return None

stock_data = get_stock_data(ticker_symbol, start_date, end_date)

if stock_data is not None and not stock_data.empty:
    # --- SMA Calculation ---
    # Create copies to avoid SettingWithCopyWarning
    data_with_sma = stock_data.copy()
    data_with_sma[f"SMA_{short_window}"] = data_with_sma["Close"].rolling(window=short_window).mean()
    data_with_sma[f"SMA_{long_window}"] = data_with_sma["Close"].rolling(window=long_window).mean()

    # --- Signal Generation ---
    # Drop NaN values after all calculations are done for plotting
    plot_data = data_with_sma.dropna()

    if not plot_data.empty:
        # Generate trading signals: 1 when short SMA > long SMA, 0 otherwise
        plot_data["Signal"] = (plot_data[f"SMA_{short_window}"] > plot_data[f"SMA_{long_window}"]).astype(int)
        plot_data["Position"] = plot_data["Signal"].diff()

        # --- Plotting ---
        st.subheader(f"{ticker_symbol} Stock Price with SMA Crossover Strategy")
        fig = go.Figure()

        # Close Price
        fig.add_trace(go.Scatter(x=plot_data.index, y=plot_data["Close"], mode="lines", name="Close Price", line=dict(color="lightgray")))

        # SMA Lines
        fig.add_trace(go.Scatter(x=plot_data.index, y=plot_data[f"SMA_{short_window}"], mode="lines", name=f"SMA {short_window}", line=dict(color="blue")))
        fig.add_trace(go.Scatter(x=plot_data.index, y=plot_data[f"SMA_{long_window}"], mode="lines", name=f"SMA {long_window}", line=dict(color="red")))

        # Buy Signals
        buy_signals = plot_data[plot_data["Position"] == 1]
        fig.add_trace(go.Scatter(x=buy_signals.index, y=buy_signals["Close"], mode="markers", marker=dict(symbol="triangle-up", size=10, color="green"), name="Buy Signal"))

        # Sell Signals
        sell_signals = plot_data[plot_data["Position"] == -1]
        fig.add_trace(go.Scatter(x=sell_signals.index, y=sell_signals["Close"], mode="markers", marker=dict(symbol="triangle-down", size=10, color="red"), name="Sell Signal"))

        fig.update_layout(xaxis_title="Date", yaxis_title="Price", xaxis_rangeslider_visible=False)
        st.plotly_chart(fig, use_container_width=True)

        # --- MLOps Section ---
        st.subheader("MLOps Integration Concept")
        st.markdown("""
        This section outlines how MLOps principles would be applied to a real automated trading strategy:

        **1. Data Versioning:** Use tools like DVC to track market data changes.
        **2. Experiment Tracking:** Use MLflow to log model training experiments.
        **3. Model Registry:** Use MLflow Model Registry for model versioning.
        **4. CI/CD for Models:** Automate model retraining and deployment with GitHub Actions.
        **5. Model Serving:** Deploy models as microservices using FastAPI or Seldon Core.
        **6. Monitoring & Alerting:** Monitor model performance with Prometheus and Grafana.
        **7. Retraining & Feedback Loops:** Automate retraining based on performance degradation.
        **8. Infrastructure as Code (IaC):** Manage infrastructure with Terraform.
        """)
    else:
        st.warning("Not enough data to display the chart after calculating moving averages. Please select a longer date range.")
else:
    st.info("Please enter a valid stock ticker and date range to see the visualization.")





