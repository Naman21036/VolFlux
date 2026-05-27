import pandas as pd
import matplotlib.pyplot as plt

class MarketRegimeDetector:

    def __init__(
        self,
        df,
        volatility_column="Volatility"
    ):

        self.regime_df = df.copy()


        self.volatility_column = (
            volatility_column
        )

        self.low_threshold = None
        self.high_threshold = None

    def calculate_thresholds(self):

        self.low_threshold = (
            self.regime_df[self.volatility_column]
            .quantile(0.33)
        )

        self.high_threshold = (
            self.regime_df[self.volatility_column]
            .quantile(0.66)
        )

        return {

            "low_threshold":
            self.low_threshold,

            "high_threshold":
            self.high_threshold
        }

    def classify_regimes(self):

        if self.low_threshold is None:

            self.calculate_thresholds()

        regimes = []

        for vol in self.regime_df[
            self.volatility_column
        ]:

            if vol < self.low_threshold:

                regimes.append(
                    "Stable"
                )

            elif vol < self.high_threshold:

                regimes.append(
                    "Neutral"
                )

            else:

                regimes.append(
                    "Risky"
                )

        self.regime_df[
            "Market_Regime"
        ] = regimes

        return self.regime_df

    def generate_risk_score(self):

        if "Market_Regime" not in (
            self.regime_df.columns
        ):

            self.classify_regimes()

        risk_scores = []

        for regime in self.regime_df[
            "Market_Regime"
        ]:

            if regime == "Stable":

                risk_scores.append(1)

            elif regime == "Neutral":

                risk_scores.append(2)

            else:

                risk_scores.append(3)

        self.regime_df[
            "Risk_Score"
        ] = risk_scores
        return self.regime_df

    def plot_regimes(self):

        if "Market_Regime" not in (
            self.regime_df.columns
        ):

            self.classify_regimes()

        plt.figure(figsize=(14, 5))

        stable = (
            self.regime_df[
                self.regime_df[
                    "Market_Regime"
                ] == "Stable"
            ]
        )

        neutral = (
            self.regime_df[
                self.regime_df[
                    "Market_Regime"
                ] == "Neutral"
            ]
        )

        risky = (
            self.regime_df[
                self.regime_df[
                    "Market_Regime"
                ] == "Risky"
            ]
        )

        plt.scatter(
            stable.index,
            stable[self.volatility_column],
            label="Stable"
        )

        plt.scatter(
            neutral.index,
            neutral[self.volatility_column],
            label="Neutral"
        )

        plt.scatter(
            risky.index,
            risky[self.volatility_column],
            label="Risky"
        )

        plt.title(
            "Market Regime Classification"
        )

        plt.xlabel("Time")

        plt.ylabel("Volatility")

        plt.legend()

        plt.grid(True)

        plt.show()

    def get_results(self):

        return self.regime_df