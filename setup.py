from setuptools import setup, find_packages

setup(
    name="VolFlux",
    version="0.1.0",
    author="Naman Gupta",
    author_email="namangupta2132@gmail.com",
    description="Quantitative Volatility Forecasting and Risk Adaptive Trading Platform",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy",
        "matplotlib",
        "seaborn",
        "plotly",
        "statsmodels",
        "arch",
        "scikit-learn",
        "fastapi",
        "uvicorn",
        "jinja2",
        "python-multipart",
        "yfinance"
    ],
    python_requires=">=3.10",
    include_package_data=True
)
