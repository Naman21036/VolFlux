import matplotlib.pyplot as plt
import seaborn as sns

from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.graphics.tsaplots import plot_pacf

from statsmodels.tsa.stattools import adfuller

from statsmodels.stats.diagnostic import het_arch



class TimeSeriesDiagnostics:

    def __init__(

        self,

        df,

        return_column="log_return"
    ):

        self.df = df.copy()

        self.return_column = (
            return_column
        )

        self.results = {}

    def stationarity_test(self):

        adf_result = adfuller(

            self.df[
                self.return_column
            ]
        )

        self.results[
            "ADF Statistic"
        ] = adf_result[0]

        self.results[
            "p-value"
        ] = adf_result[1]

        return self.results

    def plot_acf(self, lags=40):

        plt.figure(figsize=(10, 5))

        plot_acf(

            self.df[
                self.return_column
            ],

            lags=lags
        )

        plt.title(
            "ACF of Returns"
        )

        plt.show()
    
    def plot_pacf(self, lags=40):

        plt.figure(figsize=(10, 5))

        plot_pacf(

            self.df[
                self.return_column
            ],

            lags=lags
        )

        plt.title(
            "PACF of Returns"
        )

        plt.show()

    def squared_acf(self, lags=40):

        squared_returns = (

            self.df[
                self.return_column
            ] ** 2
        )

        plt.figure(figsize=(10, 5))

        plot_acf(

            squared_returns,

            lags=lags
        )

        plt.title(
            "ACF of Squared Returns"
        )

        plt.show()


    def arch_test(self):

        test_result = het_arch(

            self.df[
                self.return_column
            ]
        )

        self.results[
            "ARCH LM Statistic"
        ] = test_result[0]

        self.results[
            "ARCH p-value"
        ] = test_result[1]

        return self.results

    def distribution_plot(self):

        plt.figure(figsize=(10, 5))

        sns.histplot(

            self.df[
                self.return_column
            ],

            kde=True
        )

        plt.title(
            "Distribution of Returns"
        )

        plt.show()

    def run_diagnostics(self):

        self.stationarity_test()

        self.arch_test()

        self.distribution_plot()

        self.plot_acf()

        self.plot_pacf()

        self.squared_acf()

        return self.results