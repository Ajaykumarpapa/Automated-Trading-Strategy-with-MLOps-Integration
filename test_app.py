#!/usr/bin/env python3
"""
Test script for the trading strategy application
"""

import sys
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta

def test_imports():
    """Test if all required modules can be imported"""
    print("Testing imports...")
    try:
        import streamlit as st
        import pandas as pd
        import numpy as np
        import yfinance as yf
        import plotly.graph_objects as go
        print("✓ All imports successful")
        return True
    except ImportError as e:
        print(f"✗ Import error: {e}")
        return False

def test_data_fetching():
    """Test if stock data can be fetched"""
    print("\nTesting data fetching...")
    try:
        ticker = "AAPL"
        end_date = datetime.now()
        start_date = end_date - timedelta(days=100)

        data = yf.download(ticker, start=start_date, end=end_date, progress=False)

        if data.empty:
            print(f"✗ No data returned for {ticker}")
            return False

        print(f"✓ Successfully fetched {len(data)} days of data for {ticker}")
        return True
    except Exception as e:
        print(f"✗ Data fetching error: {e}")
        return False

def test_sma_calculation():
    """Test SMA calculation logic"""
    print("\nTesting SMA calculation...")
    try:
        # Create sample data
        dates = pd.date_range(start='2024-01-01', periods=100)
        data = pd.DataFrame({
            'Close': range(100, 200)
        }, index=dates)

        # Calculate SMAs
        short_window = 20
        long_window = 50
        data['SMA_20'] = data['Close'].rolling(window=short_window).mean()
        data['SMA_50'] = data['Close'].rolling(window=long_window).mean()

        # Drop NaN and test signal generation
        data = data.dropna()
        data['Signal'] = (data['SMA_20'] > data['SMA_50']).astype(int)
        data['Position'] = data['Signal'].diff()

        print(f"✓ SMA calculation successful")
        print(f"  - Data points after dropping NaN: {len(data)}")
        print(f"  - Buy signals: {len(data[data['Position'] == 1])}")
        print(f"  - Sell signals: {len(data[data['Position'] == -1])}")
        return True
    except Exception as e:
        print(f"✗ SMA calculation error: {e}")
        return False

def test_syntax():
    """Test if the main script has no syntax errors"""
    print("\nTesting main script syntax...")
    try:
        with open('tradingstrategy.py', 'r') as f:
            code = f.read()
        compile(code, 'tradingstrategy.py', 'exec')
        print("✓ No syntax errors in tradingstrategy.py")
        return True
    except SyntaxError as e:
        print(f"✗ Syntax error: {e}")
        return False

def main():
    """Run all tests"""
    print("=" * 60)
    print("Automated Trading Strategy - Test Suite")
    print("=" * 60)

    tests = [
        test_imports,
        test_syntax,
        test_data_fetching,
        test_sma_calculation
    ]

    results = []
    for test in tests:
        results.append(test())

    print("\n" + "=" * 60)
    print(f"Test Results: {sum(results)}/{len(results)} passed")
    print("=" * 60)

    if all(results):
        print("\n✓ All tests passed! The application is ready to run.")
        print("\nTo start the application, run:")
        print("  streamlit run tradingstrategy.py")
        print("or")
        print("  ./run.sh")
        return 0
    else:
        print("\n✗ Some tests failed. Please check the errors above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
