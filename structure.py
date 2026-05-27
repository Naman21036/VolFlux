import os

folders = [
    #"data",
    #"notebooks",
    "src"
]

src_files = [
    "__init__.py",
    "preprocessing.py",
    "diagnostics.py",
    "modeling.py",
    "forecasting.py",
    "regime.py",
    "strategy.py",
    "backtesting.py",
    "metrics.py"
]

root_files = [
    "pipeline.py",
    "main.py",
    #"setup.py",
    #"requirements.txt",
    #".gitignore",
    #"README.md"
]
for folder in folders:
    os.makedirs(folder, exist_ok=True)

for file in src_files:

    path = os.path.join("src", file)

    with open(path, "w") as f:
        f.write("")
for file in root_files:

    with open(file, "w") as f:
        f.write("")
print("Project structure created successfully!")