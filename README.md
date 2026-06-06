VolFlux

VolFlux is a quantitative volatility forecasting and risk adaptive trading platform built using Python, FastAPI, GARCH modeling, and interactive financial dashboards.

The project analyzes financial time series data, detects volatility regimes, forecasts future market volatility, generates trading signals, and evaluates strategy performance through backtesting.

Features
Volatility Forecasting using GARCH Models
Time Series Diagnostics
Regime Detection
Risk Adaptive Trading Strategy
Backtesting Engine
Performance Evaluation Metrics
Interactive FastAPI Dashboard
Live Market Data using Yahoo Finance API
Candlestick & Volatility Charts
CSV Upload Support
Multi Asset Support (Stocks, Crypto, Indices)
Pipeline Architecture
Dataset
   ↓
Preprocessing
   ↓
Time Series Diagnostics
   ↓
Volatility Modeling
   ↓
Forecasting
   ↓
Regime Detection
   ↓
Trading Strategy
   ↓
Backtesting
   ↓
Performance Evaluation
   ↓
Interactive Dashboard
Tech Stack
Backend
FastAPI
Python
Data Science & Quantitative Finance
Pandas
NumPy
Statsmodels
ARCH
Scikit Learn
Visualization
Plotly
Matplotlib
Seaborn
Frontend
HTML
CSS
Jinja2 Templates
Project Structure
VolFlux/
│
├── app.py
├── pipeline.py
├── setup.py
├── requirements.txt
│
├── data/
│
├── notebooks/
│
├── src/
│   ├── preprocessing.py
│   ├── diagnostics.py
│   ├── modeling.py
│   ├── forecasting.py
│   ├── regime.py
│   ├── strategy.py
│   ├── backtesting.py
│   └── metrics.py
│
├── templates/
│   ├── index.html
│   └── dashboard.html
│
├── static/
│   └── style.css
│
└── README.md
Installation

Clone the repository:

git clone https://github.com/Naman21036/VolFlux.git

Move into the project directory:

cd VolFlux

Create virtual environment:

python -m venv .venv

Activate virtual environment:

Windows
.venv\Scripts\activate
Linux / Mac
source .venv/bin/activate

Install dependencies:

pip install -r requirements.txt
Running the Application

Start the FastAPI server:

uvicorn app:app --reload

Open browser:

http://127.0.0.1:8000
Supported Functionalities
Dataset Upload

Upload custom CSV datasets directly from the dashboard.

Live Market Data

Analyze live assets directly from Yahoo Finance API.

Examples:

/live/AAPL
/live/BTC-USD
/live/ETH-USD
Time Series Diagnostics
Stationarity Testing
ACF Analysis
PACF Analysis
ARCH Effect Detection
Volatility Clustering Detection
Volatility Modeling
ARMA Mean Modeling
GARCH Volatility Modeling
Forecasting

Predict future market volatility for upcoming trading periods.

Regime Detection

Classify market conditions into:

Stable
Neutral
High Risk
Trading Strategy

Generate:

Buy Signals
Reduce Exposure Signals
Dynamic Position Sizing
Backtesting

Evaluate strategy performance against market benchmark.

Performance Metrics
Sharpe Ratio
Sortino Ratio
Maximum Drawdown
Total Return
Annualized Volatility
Win Rate
Example Dashboard Components
Interactive Volatility Charts
Forecast Visualization
Candlestick Charts
Equity Curves
Risk Regime Dashboard
Trading Signals
Performance Cards
Future Improvements
Real Time Streaming
WebSocket Integration
LSTM Volatility Forecasting
Portfolio Optimization
Monte Carlo Simulations
Docker Deployment
Cloud Deployment
User Authentication
Multi Asset Portfolio Analytics

Author

Naman Gupta, Ananya Hadimani
