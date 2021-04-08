import tabula
import pandas as pd

PDF_PATH = "carbon_footprint_calculator/data/2019-detailed-guide-footprint.pdf"
CSV_PATH = "carbon_footprint_calculator/data/emission-factors-accommodation.csv"


def GetAccommodationData(pdf_path=PDF_PATH, csv_path=CSV_PATH):
    # Extract tables including data on accommodation from a PDF
    tabula.convert_into(
        pdf_path,
        csv_path,
        output_format="csv",
        pages="59-60",
    )

    # Importing the data
    df = pd.read_csv(
        pdf_path,
        header=0,
        names=("Country", "Equivalent"),
        usecols=[0, 3],
    )

    # Deletion of duplication
    df.dropna(inplace=True)

    # Dictionary where the key is "Country" and the value is "Equivalent"
    return list(zip(df["Country"], df["Equivalent"]))
