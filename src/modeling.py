# src/modeling.py

import pandas as pd

from statsmodels.tsa.arima.model import ARIMA
from arch import arch_model


class VolatilityModel:

    def __init__(
        self,
        df,
        return_column="log_return"
    ):

        self.df = df.copy()

        self.return_column = return_column

        self.returns = (
            self.df[return_column]
            .dropna()
        )

        self.mean_model = None
        self.mean_fit = None

        self.residuals = None

        self.garch_model = None
        self.garch_fit = None

        self.conditional_volatility = None

        self.forecast_values = None

    def fit_mean_model(
        self,
        order=(1, 0, 1)
    ):

        self.mean_model = ARIMA(
            self.returns,
            order=order
        )

        self.mean_fit = (
            self.mean_model.fit()
        )

        self.residuals = (
            self.mean_fit.resid
        )

        return self.residuals

    def fit_garch_model(
        self,
        p=1,
        q=1
    ):

        if self.residuals is None:

            raise ValueError(
                "Run fit_mean_model() first"
            )

        self.garch_model = arch_model(
            self.residuals * 100,
            vol="GARCH",
            p=p,
            q=q
        )

        self.garch_fit = (
            self.garch_model.fit(
                disp="off"
            )
        )

        self.conditional_volatility = (
            self.garch_fit
            .conditional_volatility
        )

        return self.conditional_volatility

    def forecast_volatility(
        self,
        horizon=5
    ):

        if self.garch_fit is None:

            raise ValueError(
                "Run fit_garch_model() first"
            )

        forecast = (
            self.garch_fit
            .forecast(
                horizon=horizon
            )
        )

        self.forecast_values = (
            forecast
            .variance
            .iloc[-1]
        )

        return self.forecast_values

    def get_model_summary(self):

        return {
            "mean_model_summary":
            self.mean_fit.summary(),

            "garch_model_summary":
            self.garch_fit.summary()
        }
    def get_results(self):

        return {

            "residuals":
            self.residuals,

            "conditional_volatility":
            self.conditional_volatility,

            "forecast_values":
            self.forecast_values
        }