import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class Backtester:

    def __init__(
        self,
        df,
        market_return_col="log_return",
        strategy_return_col="Strategy_Return"
    ):

        self.df = df.copy()

        self.market_return_col = (
            market_return_col
        )

        self.strategy_return_col = (
            strategy_return_col
        )

    def compute_cumulative_returns(self):

        self.df[
            "Cumulative_Market_Return"
        ] = (

            1
            +
            self.df[
                self.market_return_col
            ]

        ).cumprod()

        self.df[
            "Cumulative_Strategy_Return"
        ] = (

            1
            +
            self.df[
                self.strategy_return_col
            ]

        ).cumprod()

        return self.df

    def compute_drawdown(self):

        rolling_max = (

            self.df[
                "Cumulative_Strategy_Return"
            ]

            .cummax()
        )

        self.df[
            "Drawdown"
        ] = (

            self.df[
                "Cumulative_Strategy_Return"
            ]

            -
            rolling_max

        ) / rolling_max

        return self.df
    
    def compute_metrics(self):

        strategy_returns = (

            self.df[
                self.strategy_return_col
            ]

            .dropna()
        )

        sharpe_ratio = (

            strategy_returns.mean()

            /

            strategy_returns.std()

        ) * np.sqrt(252)

        total_return = (

            self.df[
                "Cumulative_Strategy_Return"
            ]

            .iloc[-1]

            - 1
        )

        max_drawdown = (
            self.df[
                "Drawdown"
            ].min()
        )

        metrics = {

            "Sharpe Ratio":
            sharpe_ratio,

            "Total Return":
            total_return,

            "Maximum Drawdown":
            max_drawdown
        }

        return metrics
    
    def plot_equity_curve(self):

        plt.figure(figsize=(14, 5))

        plt.plot(

            self.df[
                "Cumulative_Market_Return"
            ],

            label="Buy & Hold"
        )

        plt.plot(

            self.df[
                "Cumulative_Strategy_Return"
            ],

            label="Volatility Strategy"
        )

        plt.title(
            "Equity Curve Comparison"
        )

        plt.xlabel("Time")

        plt.ylabel(
            "Portfolio Growth"
        )

        plt.legend()

        plt.grid(True)

        plt.show()

    def plot_drawdown(self):

        plt.figure(figsize=(14, 5))

        plt.plot(
            self.df["Drawdown"]
        )

        plt.title(
            "Strategy Drawdown"
        )

        plt.xlabel("Time")

        plt.ylabel("Drawdown")

        plt.grid(True)

        plt.show()

    def run_backtest(self):

        self.compute_cumulative_returns()

        self.compute_drawdown()

        metrics = (
            self.compute_metrics()
        )

        return metrics

    def get_results(self):

        return self.df