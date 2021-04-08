import pandas as pd

CSV_PATH = "carbon_footprint_calculator/data/emission-factors-food.csv"


def GetProductsData(csv_path=CSV_PATH):
    df = pd.read_csv(csv_path, header=0)
    return dict(zip(df["Product"], df["Equivalent"]))
