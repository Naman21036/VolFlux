from modeling import VolatilityModel
from forecasting import VolatilityForecaster
from regime import MarketRegimeDetector
from strategy import VolatilityTradingStrategy
from backtesting import Backtester
from metrics import PerformanceMetrics
import pandas as pd

df= pd.read_csv("data\\nifty50_enhanced.csv")

# Train model
model = VolatilityModel(df)

model.fit_mean_model()

model.fit_garch_model()

forecast_values = (
    model.forecast_volatility(
        horizon=5
    )
)

# Forecasting pipeline
forecaster = VolatilityForecaster(
    forecast_values
)

forecaster.create_forecast_dataframe()

forecaster.classify_volatility()

forecaster.generate_signals()

forecaster.generate_position_size()

# Plot
forecaster.plot_forecast()

# Final Output
results = forecaster.get_results()

print(results)

volatility = (
    model.conditional_volatility
)

# Initialize detector
detector = MarketRegimeDetector(
    volatility
)

# Run regime pipeline
detector.calculate_thresholds()

detector.classify_regimes()

detector.generate_risk_score()

# Plot
detector.plot_regimes()

# Results
results = detector.get_results()

print(results.head())

regime_df= pd.read_csv("data\\regime_classification.csv")
strategy = (
    VolatilityTradingStrategy(
        regime_df
    )
)

strategy.generate_signals()

strategy.generate_position_sizes()

strategy.calculate_strategy_returns()

strategy.calculate_cumulative_returns()

strategy.plot_strategy_performance()

results = strategy.get_results()

print(results.head())

strategy_df= pd.read_csv("data\\strategy_results.csv")

backtester = Backtester(
    strategy_df
)

# Run backtest
metrics = (
    backtester.run_backtest()
)

print(metrics)

# Plots
backtester.plot_equity_curve()

backtester.plot_drawdown()

# Final dataframe
results = (
    backtester.get_results()
)

print(results.head())


# strategy dataframe
metrics = PerformanceMetrics(
    strategy_df
)

results = (
    metrics.calculate_all_metrics()
)

print(results)