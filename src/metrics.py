import numpy as np
import pandas as pd


class PerformanceMetrics:

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

    def sharpe_ratio(self):

        strategy_returns = (

            self.df[
                self.strategy_return_col
            ]

            .dropna()
        )

        sharpe = (

            strategy_returns.mean()

            /

            strategy_returns.std()

        ) * np.sqrt(252)

        return sharpe

    def sortino_ratio(self):

        strategy_returns = (

            self.df[
                self.strategy_return_col
            ]

            .dropna()
        )

        downside_returns = (

            strategy_returns[
                strategy_returns < 0
            ]
        )

        downside_std = (
            downside_returns.std()
        )

        sortino = (

            strategy_returns.mean()

            /

            downside_std

        ) * np.sqrt(252)

        return sortino

    def maximum_drawdown(self):

        cumulative_returns = (

            1
            +
            self.df[
                self.strategy_return_col
            ]

        ).cumprod()

        rolling_max = (
            cumulative_returns.cummax()
        )

        drawdown = (

            cumulative_returns
            -
            rolling_max

        ) / rolling_max

        return drawdown.min()

    def total_return(self):

        cumulative_returns = (

            1
            +
            self.df[
                self.strategy_return_col
            ]

        ).cumprod()

        total_return = (
            cumulative_returns.iloc[-1]
            - 1
        )

        return total_return

    def annualized_volatility(self):

        strategy_returns = (

            self.df[
                self.strategy_return_col
            ]

            .dropna()
        )

        volatility = (

            strategy_returns.std()

            * np.sqrt(252)
        )

        return volatility

    def win_rate(self):

        strategy_returns = (

            self.df[
                self.strategy_return_col
            ]

            .dropna()
        )

        winning_trades = (
            strategy_returns > 0
        ).sum()

        total_trades = (
            len(strategy_returns)
        )

        return (
            winning_trades
            /
            total_trades
        )

    def calculate_all_metrics(self):

        metrics = {

            "Sharpe Ratio":
            self.sharpe_ratio(),

            "Sortino Ratio":
            self.sortino_ratio(),

            "Maximum Drawdown":
            self.maximum_drawdown(),

            "Total Return":
            self.total_return(),

            "Annualized Volatility":
            self.annualized_volatility(),

            "Win Rate":
            self.win_rate()
        }

        return pd.DataFrame(
            metrics.items(),
            columns=[
                "Metric",
                "Value"
            ]
        )