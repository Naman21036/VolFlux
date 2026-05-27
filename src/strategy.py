import pandas as pd
import matplotlib.pyplot as plt


class VolatilityTradingStrategy:

    def __init__(
        self,
        df,
        return_column="log_return",
        volatility_column="Volatility",
        regime_column="Market_Regime"
    ):

        self.df = df.copy()

        self.return_column = return_column

        self.volatility_column = (
            volatility_column
        )

        self.regime_column = (
            regime_column
        )

    def generate_signals(self):

        self.df[
            "volatility_change"
        ] = (
            self.df[
                self.volatility_column
            ].diff()
        )

        signals = []

        for value in self.df[
            "volatility_change"
        ]:

            if pd.isna(value):

                signals.append(
                    "Hold"
                )

            elif value < 0:

                signals.append(
                    "Buy"
                )

            else:

                signals.append(
                    "Reduce Exposure"
                )

        self.df["Signal"] = signals

        return self.df

    def generate_position_sizes(self):

        position_sizes = []

        for regime in self.df[
            self.regime_column
        ]:

            if regime == "Stable":

                position_sizes.append(
                    1.0
                )

            elif regime == "Neutral":

                position_sizes.append(
                    0.6
                )

            else:

                position_sizes.append(
                    0.2
                )

        self.df[
            "Position_Size"
        ] = position_sizes

        return self.df

    def calculate_strategy_returns(self):

        self.df[
            "Strategy_Return"
        ] = (

            self.df[
                self.return_column
            ]

            *

            self.df[
                "Position_Size"
            ]
        )

        return self.df

    def calculate_cumulative_returns(self):

        self.df[
            "Cumulative_Market_Return"
        ] = (

            1
            +
            self.df[
                self.return_column
            ]

        ).cumprod()

        self.df[
            "Cumulative_Strategy_Return"
        ] = (

            1
            +
            self.df[
                "Strategy_Return"
            ]

        ).cumprod()

        return self.df

    def plot_strategy_performance(self):

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
            "Strategy Performance"
        )

        plt.xlabel("Time")

        plt.ylabel(
            "Cumulative Returns"
        )

        plt.legend()

        plt.grid(True)

        plt.show()

    def get_results(self):
        return self.df