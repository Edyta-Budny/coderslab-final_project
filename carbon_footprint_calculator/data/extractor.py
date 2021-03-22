import tabula
import pandas as pd


def GetAccommodationData():
    # Extract tables including data on accommodation from a PDF
    tabula.convert_into(
        "carbon_footprint_calculator/data/2019-detailed-guide-footprint.pdf",
        "carbon_footprint_calculator/data/emission-factors-accommodation.csv",
        output_format="csv",
        pages="59-60",
    )

    # Importing the data
    df = pd.read_csv(
        "carbon_footprint_calculator/data/emission-factors-accommodation.csv",
        header=0,
        names=("Country", "Equivalent"),
        usecols=[0, 3],
    )

    # Deletion of duplication
    df.dropna(inplace=True)

    # Dictionary where the key is "Country" and the value is "Equivalent"
    accommodation_data = list(zip(df["Country"], df["Equivalent"]))

    return accommodation_data
