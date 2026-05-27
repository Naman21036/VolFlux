import pandas as pd
from pipeline import VolatilityPipeline

# Load cleaned dataset
df = pd.read_csv("data\\aapl_data_enhanced.csv")

# Initialize pipeline
pipeline = VolatilityPipeline(df)

# Run complete pipeline
results = pipeline.run_pipeline()

# Outputs
print(results["performance_metrics"])
print(results["final_dataframe"].head())
