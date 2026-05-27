# app.py

from fastapi import FastAPI
from fastapi import Request
from fastapi import UploadFile
from fastapi import File

from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

import pandas as pd
import numpy as np

import plotly.express as px
import plotly.graph_objects as go

import yfinance as yf

from pipeline import VolatilityPipeline

# FASTAPI APP

app = FastAPI()

# TEMPLATES

templates = Jinja2Templates(
    directory="templates"
)

# STATIC FILES

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

# DATA PREPARATION

def prepare_data(df):

    # Lowercase columns
    df.columns = [

        col.lower()

        for col in df.columns
    ]

    # Handle datetime
    if "date" in df.columns:

        df["date"] = pd.to_datetime(
            df["date"]
        )

        df.set_index(
            "date",
            inplace=True
        )

    # Compute log returns
    if "log_return" not in df.columns:

        df["log_return"] = np.log(

            df["close"]

            /

            df["close"].shift(1)
        )

    # Drop missing rows
    df.dropna(inplace=True)

    return df

# DASHBOARD GENERATOR

def generate_dashboard(df):

    # Prepare data
    df = prepare_data(df)

    # Run pipeline
    pipeline = VolatilityPipeline(df)

    results = pipeline.run_pipeline()

    final_df = results["final_dataframe"]

    metrics_df = results["performance_metrics"]

    diagnostics = results["diagnostics"]

    # METRICS DICTIONARY

    metrics = {}

    for _, row in metrics_df.iterrows():

        metrics[
            row["Metric"]
        ] = round(
            row["Value"],
            4
        )

    # VOLATILITY CHART

    fig1 = px.line(

        final_df,

        y="Volatility",

        title="Market Volatility",

        template="plotly_dark"
    )

    volatility_chart = (
        fig1.to_html(
            full_html=False
        )
    )

    # EQUITY CURVE

    fig2 = px.line(

        final_df,

        y=[
            "Cumulative_Market_Return",
            "Cumulative_Strategy_Return"
        ],

        title="Strategy vs Buy & Hold",

        template="plotly_dark"
    )

    equity_chart = (
        fig2.to_html(
            full_html=False
        )
    )

    # FORECAST CHART

    forecast_values = (
        pipeline.model.forecast_values
    )

    forecast_df = pd.DataFrame({

        "Day":
        range(
            1,
            len(forecast_values) + 1
        ),

        "Forecast":
        forecast_values.values
    })

    fig3 = px.line(

        forecast_df,

        x="Day",

        y="Forecast",

        title="Future Volatility Forecast",

        template="plotly_dark"
    )

    forecast_chart = (
        fig3.to_html(
            full_html=False
        )
    )

    # CANDLESTICK CHART

    candlestick_chart = None

    required_columns = [
        "open",
        "high",
        "low",
        "close"
    ]

    if all(
        col in final_df.columns
        for col in required_columns
    ):

        fig4 = go.Figure(

            data=[

                go.Candlestick(

                    x=final_df.index,

                    open=final_df["open"],

                    high=final_df["high"],

                    low=final_df["low"],

                    close=final_df["close"]
                )
            ]
        )

        fig4.update_layout(

            title="Candlestick Chart",

            template="plotly_dark"
        )

        candlestick_chart = (
            fig4.to_html(
                full_html=False
            )
        )

    # LATEST MARKET STATE

    latest_regime = (
        final_df[
            "Market_Regime"
        ].iloc[-1]
    )

    latest_signal = (
        final_df[
            "Signal"
        ].iloc[-1]
    )

    # RETURN DASHBOARD DATA

    return {

        "metrics":
        metrics,

        "diagnostics":
        diagnostics,

        "volatility_chart":
        volatility_chart,

        "equity_chart":
        equity_chart,

        "forecast_chart":
        forecast_chart,

        "candlestick_chart":
        candlestick_chart,

        "regime":
        latest_regime,

        "signal":
        latest_signal
    }


# HOME PAGE

@app.get("/")
def home(request: Request):

    return templates.TemplateResponse(

        request=request,

        name="index.html"
    )

# CSV UPLOAD


@app.post("/upload")
async def upload_csv(

    request: Request,

    file: UploadFile = File(...)
):

    try:

        # Save uploaded file
        file_path = (
            f"data/{file.filename}"
        )

        with open(file_path, "wb") as f:

            content = await file.read()

            f.write(content)

        # Load dataset
        df = pd.read_csv(file_path)

        # Generate dashboard
        dashboard_data = (
            generate_dashboard(df)
        )

        return templates.TemplateResponse(

            request=request,

            name="dashboard.html",

            context=dashboard_data
        )

    except Exception as e:

        return {

            "error":
            str(e)
        }

# DEFAULT DATASET

@app.get("/run")
def run_pipeline(request: Request):

    try:

        df = pd.read_csv(
            "data/nifty50_enhanced.csv"
        )

        dashboard_data = (
            generate_dashboard(df)
        )

        return templates.TemplateResponse(

            request=request,

            name="dashboard.html",

            context=dashboard_data
        )

    except Exception as e:

        return {

            "error":
            str(e)
        }

# LIVE MARKET DATA

@app.get("/live/{ticker}")
def live_market_data(

    request: Request,

    ticker: str
):

    try:

        # Download market data
        df = yf.download(

            ticker,

            period="2y",

            interval="1d"
        )

        df.reset_index(inplace=True)

        # Generate dashboard
        dashboard_data = (
            generate_dashboard(df)
        )

        return templates.TemplateResponse(

            request=request,

            name="dashboard.html",

            context=dashboard_data
        )

    except Exception as e:

        return {

            "error":
            str(e)
        }
    