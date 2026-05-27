import pandas as pd
from src.modeling import VolatilityModel
from src.forecasting import VolatilityForecaster
from src.regime import MarketRegimeDetector
from src.strategy import VolatilityTradingStrategy
from src.backtesting import Backtester
from src.metrics import PerformanceMetrics


class VolatilityPipeline:

    def __init__(
        self,
        df,
        return_column="log_return"
    ):

        self.df = df.copy()

        self.return_column = (
            return_column
        )

        self.model = None

        self.forecaster = None

        self.regime_detector = None

        self.strategy = None

        self.backtester = None

        self.metrics = None

        self.final_df = None

    # MODELING STAGE


    def run_modeling(
        self,
        arma_order=(1, 0, 1),
        garch_p=1,
        garch_q=1,
        forecast_horizon=5
    ):

        self.model = VolatilityModel(
            self.df,
            return_column=self.return_column
        )

        # Mean Model
        self.model.fit_mean_model(
            order=arma_order
        )

        # GARCH Model
        conditional_volatility = (
            self.model.fit_garch_model(
                p=garch_p,
                q=garch_q
            )
        )

        # Add volatility to dataframe
        self.df[
            "Volatility"
        ] = conditional_volatility.values

        return conditional_volatility
    
    # FORECASTING STAGE


    def run_forecasting(
        self,
        forecast_horizon=5
    ):

        forecast_values = (
            self.model.forecast_volatility(
                horizon=forecast_horizon
            )
        )

        self.forecaster = (
            VolatilityForecaster(
                forecast_values
            )
        )

        self.forecaster.create_forecast_dataframe()

        self.forecaster.classify_volatility()

        self.forecaster.generate_signals()

        self.forecaster.generate_position_size()

        forecast_df = (
            self.forecaster.get_results()
        )

        return forecast_df

    # REGIME DETECTION

    def run_regime_detection(self):

        self.regime_detector = (
            MarketRegimeDetector(
                self.df["Volatility"]
            )
        )

        self.regime_detector.calculate_thresholds()

        regime_df = (
            self.regime_detector
            .classify_regimes()
        )

        regime_df = (
            self.regime_detector
            .generate_risk_score()
        )

        # Add returns back
        regime_df[
            self.return_column
        ] = (
            self.df[
                self.return_column
            ]
        )

        self.final_df = regime_df

        return self.final_df

    # STRATEGY STAGE

    def run_strategy(self):

        self.strategy = (
            VolatilityTradingStrategy(
                self.final_df
            )
        )

        self.strategy.generate_signals()

        self.strategy.generate_position_sizes()

        strategy_df = (
            self.strategy
            .calculate_strategy_returns()
        )

        strategy_df = (
            self.strategy
            .calculate_cumulative_returns()
        )

        self.final_df = strategy_df

        return self.final_df

    
    # BACKTESTING STAGE

    def run_backtesting(self):

        self.backtester = (
            Backtester(
                self.final_df
            )
        )

        metrics = (
            self.backtester
            .run_backtest()
        )

        self.final_df = (
            self.backtester
            .get_results()
        )

        return metrics

    # PERFORMANCE METRICS

    def run_metrics(self):

        self.metrics = (
            PerformanceMetrics(
                self.final_df
            )
        )

        metrics_df = (
            self.metrics
            .calculate_all_metrics()
        )

        return metrics_df


    # COMPLETE PIPELINE
 

    def run_pipeline(self):

        print(
            "\nRunning Modeling Stage..."
        )

        self.run_modeling()

        print(
            "Modeling Completed"
        )
        print(
            "\nRunning Forecasting..."
        )

        forecast_df = (
            self.run_forecasting()
        )

        print(
            "Forecasting Completed"
        )

        print(
            "\nRunning Regime Detection..."
        )

        self.run_regime_detection()

        print(
            "Regime Detection Completed"
        )

        print(
            "\nRunning Trading Strategy..."
        )

        self.run_strategy()

        print(
            "Trading Strategy Completed"
        )

        print(
            "\nRunning Backtesting..."
        )

        backtest_metrics = (
            self.run_backtesting()
        )

        print(
            "Backtesting Completed"
        )

        print(
            "\nCalculating Metrics..."
        )

        metrics_df = (
            self.run_metrics()
        )

        print(
            "Metrics Calculation Completed"
        )

        return {

            "final_dataframe":
            self.final_df,

            "backtest_metrics":
            backtest_metrics,

            "performance_metrics":
            metrics_df
        }