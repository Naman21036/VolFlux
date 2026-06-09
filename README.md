# VolFlux 📈

**Volatility Forecasting & Risk Adaptive Trading Platform**

VolFlux is an end to end quantitative finance platform that forecasts market volatility, detects volatility regimes, generates risk adaptive trading signals, and evaluates strategy performance through backtesting.

Built using FastAPI, GARCH modeling, statistical time series analysis, and interactive financial dashboards, VolFlux transforms raw market data into actionable risk insights for traders, analysts, and quantitative researchers.

---

## 🌐 Live Demo

**Application:** https://volflux-ce323960.fastapicloud.dev/

**GitHub Repository:** https://github.com/Naman21036/VolFlux

---

## 🚀 Key Features

### Market Data Processing

* CSV based market data ingestion
* Live market data integration using Yahoo Finance
* Automated preprocessing and feature engineering
* Log return computation
* Missing value handling

### Time Series Diagnostics

* Augmented Dickey Fuller (ADF) Stationarity Test
* Autocorrelation Function (ACF) Analysis
* Partial Autocorrelation Function (PACF) Analysis
* Volatility Clustering Detection
* ARCH Effect Detection

### Volatility Modeling

* ARMA Mean Modeling
* GARCH(1,1) Volatility Modeling
* Conditional Volatility Estimation
* Multi Step Volatility Forecasting

### Market Regime Detection

* Stable Market Regime
* Neutral Market Regime
* Risky Market Regime

### Trading Engine

* Dynamic Position Sizing
* Risk Adaptive Trading Signals
* Volatility Driven Exposure Control
* Buy / Reduce Exposure Recommendations

### Backtesting & Evaluation

* Strategy Backtesting
* Benchmark Comparison
* Equity Curve Analysis
* Risk Adjusted Performance Evaluation

### Interactive Dashboard

* Volatility Visualization
* Forecast Visualization
* Candlestick Charts
* Strategy Performance Tracking
* Market Regime Dashboard

---

## 🏗 System Architecture

```text
Market Dataset
      │
      ▼
Preprocessing
      │
      ▼
Time Series Diagnostics
      │
      ▼
ARMA + GARCH Modeling
      │
      ▼
Volatility Forecasting
      │
      ▼
Market Regime Detection
      │
      ▼
Trading Signal Generation
      │
      ▼
Backtesting
      │
      ▼
Performance Evaluation
      │
      ▼
Interactive Dashboard
```

---

## 🛠 Tech Stack

### Backend

* FastAPI
* Python

### Quantitative Finance

* Statsmodels
* ARCH
* NumPy
* Pandas

### Machine Learning & Analytics

* Scikit Learn

### Visualization

* Plotly
* Matplotlib
* Seaborn

### Frontend

* HTML
* CSS
* Jinja2

### Data Sources

* Yahoo Finance API

---

## 📂 Project Structure

```text
VolFlux
│
├── app.py
├── pipeline.py
├── setup.py
├── requirements.txt
│
├── data/
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
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/Naman21036/VolFlux.git
cd VolFlux
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Environment

Windows:

```bash
.venv\Scripts\activate
```

Linux / macOS:

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Start the FastAPI server:

```bash
uvicorn app:app --reload
```

Open:

```text
http://127.0.0.1:8000
```

---

## 📊 Supported Functionalities

### Dataset Upload

Upload custom market datasets directly through the dashboard.

### Live Market Analysis

Examples:

```text
/live/AAPL
/live/BTC-USD
/live/ETH-USD
```

### Diagnostics Dashboard

* Stationarity Testing
* ACF Analysis
* PACF Analysis
* ARCH Detection
* Volatility Clustering Detection

### Forecasting Engine

Predict future market volatility for upcoming trading sessions.

### Regime Classification

| Regime  | Market Condition    |
| ------- | ------------------- |
| Stable  | Low Volatility      |
| Neutral | Moderate Volatility |
| Risky   | High Volatility     |

### Trading Signal Engine

| Market State    | Action            |
| --------------- | ----------------- |
| Low Volatility  | Increase Exposure |
| Neutral         | Hold              |
| High Volatility | Reduce Exposure   |

---

## 📈 Performance Metrics

VolFlux evaluates strategies using:

* Sharpe Ratio
* Sortino Ratio
* Maximum Drawdown
* Annualized Return
* Annualized Volatility
* Win Rate
* Total Return

---

## 🔮 Future Roadmap

* LSTM Based Volatility Forecasting
* EGARCH & TGARCH Models
* Real Time Streaming Data
* WebSocket Integration
* Portfolio Optimization
* Monte Carlo Risk Simulation
* Docker Containerization
* Cloud Native Deployment
* Multi Asset Portfolio Analytics
* User Authentication & Profiles

---

## 👥 Contributors

### Naman Gupta

* Quantitative Research
* System Design
* Backend Development

### Ananya Hadimani

* Research
* Analytics
* Project Development

---

## ⭐ Acknowledgements

This project was developed to explore practical applications of quantitative finance, volatility forecasting, statistical modeling, and risk adaptive trading systems using modern Python based technologies.
