import pandas as pd
import numpy as np


class DataPreprocessor:

    def __init__(self, df):

        self.df = df.copy()

    def standardize_columns(self):

        self.df.columns = [

            col.lower().strip()

            for col in self.df.columns
        ]

        return self.df

    def process_datetime(self):

        if "date" in self.df.columns:

            self.df["date"] = pd.to_datetime(
                self.df["date"]
            )

            self.df.set_index(
                "date",
                inplace=True
            )
            self.df = self.df.asfreq("B")

        return self.df

    def handle_missing_values(self):

        self.df = self.df.bfill()

        return self.df

    def compute_log_returns(self):

        self.df["log_return"] = np.log(

            self.df["close"]

            /

            self.df["close"].shift(1)
        )

        self.df.dropna(inplace=True)

        return self.df

    def run_pipeline(self):

        self.standardize_columns()

        self.process_datetime()

        self.handle_missing_values()

        self.compute_log_returns()

        return self.df