import pandas as pd

CSV_PATH = "carbon_footprint_calculator/data/emission-factors-travel.csv"


def GetTravelData(csv_path=CSV_PATH):

    # Importing the data
    df = pd.read_csv(
        csv_path,
        header=0,
    )

    # Dictionary where the key is "Means of transport" and the value is
    # "Equivalent"
    return list(zip(df["Means of transport"], df["Equivalent"]))

