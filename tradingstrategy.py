import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import plotly.graph_objects as go
from datetime import datetime, timedelta

st.set_page_config(layout="wide")

st.title("Automated Trading Strategy with MLOps Integration Concept")
st.write("This application demonstrates a simplified automated trading strategy (SMA Crossover) and outlines how MLOps principles would be integrated for a production-ready system.")

# Sidebar for user input
st.sidebar.header("Strategy Parameters")
ticker_symbol = st.sidebar.text_input("Enter Stock Ticker (e.g., AAPL, MSFT)", "AAPL").upper()
start_date = st.sidebar.date_input("Start Date", datetime.now() - timedelta(days=365*2))
end_date = st.sidebar.date_input("End Date", datetime.now())

short_window = st.sidebar.slider("Short Moving Average Window", 5, 50, 20)
long_window = st.sidebar.slider("Long Moving Average Window", 20, 200, 50)

# Fetch data
@st.cache_data
def get_stock_data(ticker, start, end):
    try:
        data = yf.download(ticker, start=start, end=end)
        return data
    except Exception as e:
        st.error(f"Error fetching data for {ticker}: {e}")
        return None

stock_data = get_stock_data(ticker_symbol, start_date, end_date)

if stock_data is not None and not stock_data.empty:
    st.subheader(f"Historical Data for {ticker_symbol}")
    st.dataframe(stock_data.tail())

    # Calculate Moving Averages
    stock_data["SMA_" + str(short_window)] = stock_data["Close"].rolling(window=short_window).mean()
    stock_data["SMA_" + str(long_window)] = stock_data["Close"].rolling(window=long_window).mean()

    # Drop NaN values that result from rolling mean calculation to ensure plotting works correctly
    # This ensures that only rows with valid SMA values are used for plotting and signal generation.
    stock_data.dropna(inplace=True)

    if not stock_data.empty:
        # Generate Trading Signals
        stock_data["Signal"] = 0
        # Ensure we only access valid indices after dropping NaNs
        stock_data["Signal"] = np.where(stock_data["SMA_" + str(short_window)] > stock_data["SMA_" + str(long_window)], 1, 0)
        stock_data["Position"] = stock_data["Signal"].diff()

        st.subheader("Trading Strategy Visualization (SMA Crossover)")
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data["Close"], mode="lines", name="Close Price", line=dict(color="lightgray")))
        fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data["SMA_" + str(short_window)], mode="lines", name=f"SMA {short_window}", line=dict(color="blue")))
        fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data["SMA_" + str(long_window)], mode="lines", name=f"SMA {long_window}", line=dict(color="red")))

        # Add buy signals
        buy_signals = stock_data[stock_data["Position"] == 1]
        fig.add_trace(go.Scatter(
            x=buy_signals.index,
            y=buy_signals["Close"],
            mode="markers",
            marker=dict(symbol="triangle-up", size=10, color="green"),
            name="Buy Signal"
        ))

        # Add sell signals
        sell_signals = stock_data[stock_data["Position"] == -1]
        fig.add_trace(go.Scatter(
            x=sell_signals.index,
            y=sell_signals["Close"],
            mode="markers",
            marker=dict(symbol="triangle-down", size=10, color="red"),
            name="Sell Signal"
        ))

        fig.update_layout(title=f"{ticker_symbol} Stock Price with SMA Crossover Strategy",
                          xaxis_title="Date",
                          yaxis_title="Price",
                          xaxis_rangeslider_visible=False)
        st.plotly_chart(fig)

        st.subheader("MLOps Integration Concept")
        st.markdown(
            "This section outlines how MLOps principles would be applied to a real automated trading strategy:"
            "\n\n" 
            "**1. Data Versioning:** Use tools like DVC (Data Version Control) to track changes in historical market data, ensuring reproducibility of model training.\n"
            "**2. Model Training & Experiment Tracking:** Train deep learning models (e.g., LSTMs for price prediction) using frameworks like TensorFlow or PyTorch. Track experiments, parameters, and metrics with MLflow.\n"
            "**3. Model Registry:** Register trained models in MLflow Model Registry, allowing for version control and easy deployment of specific model versions.\n"
            "**4. CI/CD for Models:** Implement Continuous Integration/Continuous Deployment pipelines (e.g., using GitHub Actions, Jenkins, or GitLab CI) to automate model retraining, testing, and deployment to production environments.\n"
            "**5. Model Serving:** Deploy models as microservices using tools like TensorFlow Serving, Seldon Core, or FastAPI, making them accessible for real-time inference in the trading system.\n"
            "**6. Monitoring & Alerting:** Continuously monitor model performance (e.g., prediction accuracy, trading strategy profitability) and data drift in production. Set up alerts for performance degradation or anomalies using tools like Prometheus and Grafana.\n"
            "**7. Retraining & Feedback Loops:** Establish automated retraining pipelines triggered by performance degradation or new data availability. Incorporate feedback from live trading results to improve future model versions.\n"
            "**8. Infrastructure as Code (IaC):** Manage the underlying infrastructure (e.g., Kubernetes clusters for model serving) using IaC tools like Terraform or Ansible.\n"
        )
    else:
        st.warning(f"Not enough data available after calculating moving averages for {ticker_symbol}. Please try a longer date range or different parameters.")
else:
    st.warning(f"Could not retrieve data for {ticker_symbol}. Please check the ticker symbol and date range.")






