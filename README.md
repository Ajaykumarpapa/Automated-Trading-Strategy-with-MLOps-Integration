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

### Option 1: Run Locally

Run the Streamlit application:

```bash
streamlit run tradingstrategy.py
```

Or use the provided run script:

```bash
./run.sh
```

The application will open in your default web browser at `http://localhost:8501`.

### Option 2: Run with Docker

Build and run using Docker:

```bash
docker build -t trading-strategy .
docker run -p 8501:8501 trading-strategy
```

Or use Docker Compose:

```bash
docker-compose up
```

The application will be available at `http://localhost:8501`.

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
├── tradingstrategy.py       # Main Streamlit application
├── config.py               # Configuration settings
├── test_app.py            # Test suite
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── DEPLOYMENT.md        # Deployment guide
│
├── Docker Files
├── Dockerfile             # Docker container definition
├── docker-compose.yml     # Docker Compose configuration
├── .dockerignore         # Docker ignore rules
│
├── Cloud Deployment
├── Procfile              # Heroku configuration
├── setup.sh             # Heroku setup script
├── app.yaml            # Google App Engine config
├── .env.example       # Environment variables template
│
├── Kubernetes
├── k8s/
│   ├── deployment.yaml   # K8s deployment manifest
│   ├── ingress.yaml     # K8s ingress configuration
│   └── README.md       # K8s deployment guide
│
├── Deployment Scripts
├── scripts/
│   ├── deploy-heroku.sh  # Heroku deployment
│   ├── deploy-docker.sh  # Docker Hub deployment
│   ├── deploy-aws.sh    # AWS EC2 deployment
│   └── deploy-gcp.sh   # Google Cloud deployment
│
├── Configuration
├── .streamlit/
│   └── config.toml      # Streamlit configuration
├── .github/
│   └── workflows/
│       └── ci.yml       # CI/CD pipeline
├── .gitignore          # Git ignore rules
└── run.sh             # Application runner script
```

## Dependencies

### Core Dependencies
- **streamlit**: Web application framework
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computing
- **yfinance**: Stock market data fetching
- **plotly**: Interactive visualizations

### Additional Dependencies
- **beautifulsoup4**: HTML parsing for data scraping
- **curl-cffi**: HTTP client for yfinance
- **websockets**: Real-time data support
- **lxml**: XML/HTML processing

See `requirements.txt` for complete list with version constraints.

## Disclaimer

This application is for educational purposes only. It is not financial advice. Always do your own research and consult with a qualified financial advisor before making investment decisions.

## Testing

Run the test suite to verify the installation:

```bash
python test_app.py
```

This will test:
- Module imports
- Syntax validation
- Data fetching capabilities
- SMA calculation logic

## CI/CD Pipeline

The project includes a GitHub Actions workflow (`.github/workflows/ci.yml`) that automatically:
- Runs tests on push/pull requests
- Performs code quality checks
- Builds Docker images
- Can be extended for automated deployments

## Deployment

Ready to deploy your application? See [DEPLOYMENT.md](DEPLOYMENT.md) for comprehensive deployment guides.

### Quick Deploy Options

**🚀 Streamlit Cloud (Easiest - Free)**
```bash
# 1. Push code to GitHub (done!)
# 2. Go to share.streamlit.io
# 3. Connect repository
# 4. Deploy in 2 minutes!
```

**🐳 Docker (Recommended)**
```bash
# Use automated script
./scripts/deploy-docker.sh yourusername

# Or manually
docker build -t trading-strategy .
docker run -p 8501:8501 trading-strategy
```

**☁️ Cloud Platforms**
```bash
# Heroku
./scripts/deploy-heroku.sh your-app-name

# AWS EC2
./scripts/deploy-aws.sh ec2-ip-address key-file.pem

# Google Cloud Run
./scripts/deploy-gcp.sh your-project-id
```

### Deployment Files

- `DEPLOYMENT.md` - Complete deployment guide for all platforms
- `Procfile` - Heroku configuration
- `setup.sh` - Heroku setup script
- `app.yaml` - Google App Engine configuration
- `k8s/` - Kubernetes manifests
- `scripts/` - Automated deployment scripts

For detailed instructions, troubleshooting, and best practices, see **[DEPLOYMENT.md](DEPLOYMENT.md)**.

## Future Enhancements

- [ ] Implement additional trading strategies (RSI, MACD, Bollinger Bands)
- [ ] Add backtesting functionality with performance metrics
- [ ] Integrate machine learning models for prediction
- [ ] Add portfolio management features
- [ ] Implement real MLOps pipeline with MLflow tracking
- [ ] Add comprehensive unit tests and integration tests
- [x] Create Docker containerization
- [ ] Add database for storing historical data
- [ ] Implement real-time streaming data
- [ ] Add authentication and user management
- [ ] Create REST API endpoints

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
