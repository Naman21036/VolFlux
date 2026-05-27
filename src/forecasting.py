import pandas as pd
import matplotlib.pyplot as plt


class VolatilityForecaster:

    def __init__(
        self,
        forecast_values
    ):

        self.forecast_values = (
            forecast_values
        )

        self.forecast_df = None

    def create_forecast_dataframe(self):

        self.forecast_df = pd.DataFrame({

            "Day":
            range(
                1,
                len(self.forecast_values) + 1
            ),

            "Forecasted_Volatility":
            self.forecast_values.values
        })

        return self.forecast_df

    def classify_volatility(self):

        if self.forecast_df is None:

            raise ValueError(
                "Run create_forecast_dataframe() first"
            )

        mean_volatility = (
            self.forecast_df[
                "Forecasted_Volatility"
            ].mean()
        )

        conditions = []

        for value in self.forecast_df[
            "Forecasted_Volatility"
        ]:

            if value < mean_volatility * 0.8:

                conditions.append(
                    "Low Risk"
                )

            elif value < mean_volatility * 1.2:

                conditions.append(
                    "Neutral"
                )

            else:

                conditions.append(
                    "High Risk"
                )

        self.forecast_df[
            "Market_Regime"
        ] = conditions

        return self.forecast_df

    def generate_signals(self):

        if self.forecast_df is None:

            raise ValueError(
                "Run classify_volatility() first"
            )

        signals = []

        previous_vol = None

        for current_vol in self.forecast_df[
            "Forecasted_Volatility"
        ]:

            if previous_vol is None:

                signals.append(
                    "Hold"
                )

            elif current_vol < previous_vol:

                signals.append(
                    "Buy"
                )

            else:

                signals.append(
                    "Reduce Exposure"
                )

            previous_vol = current_vol

        self.forecast_df[
            "Signal"
        ] = signals

        return self.forecast_df

    def generate_position_size(self):

        if self.forecast_df is None:

            raise ValueError(
                "Run generate_signals() first"
            )

        position_sizes = []

        for regime in self.forecast_df[
            "Market_Regime"
        ]:

            if regime == "Low Risk":

                position_sizes.append(1.0)

            elif regime == "Neutral":

                position_sizes.append(0.6)

            else:

                position_sizes.append(0.2)

        self.forecast_df[
            "Position_Size"
        ] = position_sizes

        return self.forecast_df

    def plot_forecast(self):

        if self.forecast_df is None:

            raise ValueError(
                "Run create_forecast_dataframe() first"
            )

        plt.figure(figsize=(10, 5))

        plt.plot(
            self.forecast_df["Day"],
            self.forecast_df[
                "Forecasted_Volatility"
            ],
            marker="o"
        )

        plt.title(
            "Volatility Forecast"
        )

        plt.xlabel("Forecast Horizon")

        plt.ylabel(
            "Forecasted Volatility"
        )

        plt.grid(True)

        plt.show()

    def get_results(self):

        return self.forecast_df