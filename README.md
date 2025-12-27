# Automated Trading Strategy with MLOps Integration

An automated trading strategy visualization tool using Simple Moving Average (SMA) crossover strategy with MLOps integration concepts.

## Features

- **Real-time Stock Data**: Fetch and display stock data using Yahoo Finance API
- **SMA Crossover Strategy**: Implement and visualize trading signals based on SMA crossover
- **Interactive Dashboard**: Built with Streamlit for easy interaction and visualization
- **Buy/Sell Signals**: Visual indicators for entry and exit points
- **MLOps Concepts**: Overview of MLOps integration for production-ready trading systems

## Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd Automated-Trading-Strategy-with-MLOps-Integration
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the Streamlit application:

```bash
streamlit run tradingstrategy.py
```

The application will open in your default web browser at `http://localhost:8501`.

### How to Use

1. **Enter Stock Ticker**: Input the stock symbol (e.g., AAPL, GOOGL, TSLA)
2. **Select Date Range**: Choose start and end dates for historical data
3. **Adjust SMA Parameters**:
   - Short SMA Window: Faster moving average (default: 20 days)
   - Long SMA Window: Slower moving average (default: 50 days)
4. **View Results**: The chart displays:
   - Stock closing price
   - Short and long SMAs
   - Buy signals (green triangles)
   - Sell signals (red triangles)

## Trading Strategy

The **SMA Crossover Strategy** works as follows:

- **Buy Signal**: When the short-term SMA crosses above the long-term SMA
- **Sell Signal**: When the short-term SMA crosses below the long-term SMA

This is a momentum-based strategy that aims to capture trending moves in the market.

## MLOps Integration Concepts

The application demonstrates how MLOps principles can be applied to trading strategies:

1. **Data Versioning**: Track market data changes with DVC
2. **Experiment Tracking**: Log model training with MLflow
3. **Model Registry**: Version control for trading models
4. **CI/CD Pipeline**: Automated testing and deployment
5. **Model Serving**: Deploy as microservices using FastAPI
6. **Monitoring**: Track model performance with Prometheus/Grafana
7. **Automated Retraining**: Trigger retraining based on performance metrics
8. **Infrastructure as Code**: Manage infrastructure with Terraform

## Project Structure

```
.
├── tradingstrategy.py    # Main Streamlit application
├── requirements.txt      # Python dependencies
├── README.md            # Project documentation
└── .gitignore          # Git ignore rules
```

## Dependencies

- streamlit: Web application framework
- pandas: Data manipulation
- numpy: Numerical computing
- yfinance: Stock market data
- plotly: Interactive visualizations

## Disclaimer

This application is for educational purposes only. It is not financial advice. Always do your own research and consult with a qualified financial advisor before making investment decisions.

## Future Enhancements

- [ ] Implement additional trading strategies (RSI, MACD, Bollinger Bands)
- [ ] Add backtesting functionality
- [ ] Integrate machine learning models for prediction
- [ ] Add portfolio management features
- [ ] Implement real MLOps pipeline with MLflow
- [ ] Add unit tests and integration tests
- [ ] Create Docker containerization
- [ ] Add database for storing historical data

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
