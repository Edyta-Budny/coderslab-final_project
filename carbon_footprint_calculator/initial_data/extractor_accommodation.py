from functools import lru_cache

import tabula
import pandas as pd

PDF_PATH = "carbon_footprint_calculator/initial_data/2019-detailed-guide" \
           "-footprint-pages-59-60.pdf"
CSV_PATH = "carbon_footprint_calculator/initial_data/emission-factors" \
           "-accommodation.csv"


@lru_cache
def GetAccommodationData(pdf_path=PDF_PATH, csv_path=CSV_PATH):

    # Extract tables including data on accommodation from a PDF
    tabula.convert_into(pdf_path, csv_path, pages="all")

    # Importing the data
    df = pd.read_csv(csv_path, header=0, names=("Country", "Equivalent"),
                     usecols=[0, 3])

    # Deletion of duplication
    df.dropna(inplace=True)

    # Dictionary where the key is "Country" and the value is "Equivalent"
    return dict(zip(df["Country"], df["Equivalent"]))
