import pandas as pd

CSV_PATH = "carbon_footprint_calculator/data/emission-factors-travel.csv"


def GetTravelData(csv_path=CSV_PATH):
    df = pd.read_csv(csv_path, header=0)
    return list(zip(df["Means of transport"], df["Equivalent"]))
