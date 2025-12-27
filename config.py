"""
Configuration file for Trading Strategy Application
This file contains all configurable parameters for the application.
"""

# Application Settings
APP_TITLE = "Trading Strategy Visualization (SMA Crossover)"
APP_LAYOUT = "wide"

# Default Trading Parameters
DEFAULT_TICKER = "AAPL"
DEFAULT_LOOKBACK_YEARS = 2
DEFAULT_SHORT_WINDOW = 20
DEFAULT_LONG_WINDOW = 50

# SMA Window Ranges
SHORT_WINDOW_MIN = 5
SHORT_WINDOW_MAX = 50
LONG_WINDOW_MIN = 20
LONG_WINDOW_MAX = 200

# Chart Settings
CHART_COLORS = {
    "close_price": "lightgray",
    "short_sma": "blue",
    "long_sma": "red",
    "buy_signal": "green",
    "sell_signal": "red"
}

MARKER_SETTINGS = {
    "buy": {
        "symbol": "triangle-up",
        "size": 10
    },
    "sell": {
        "symbol": "triangle-down",
        "size": 10
    }
}

# Data Fetching Settings
YFINANCE_SETTINGS = {
    "progress": False,
    "auto_adjust": True
}

# MLOps Settings (for future implementation)
MLFLOW_TRACKING_URI = "http://localhost:5000"
MODEL_REGISTRY_NAME = "trading_strategy_models"
EXPERIMENT_NAME = "sma_crossover_strategy"

# Monitoring Settings
ENABLE_LOGGING = True
LOG_LEVEL = "INFO"
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
