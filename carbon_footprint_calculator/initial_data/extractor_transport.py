from functools import lru_cache

import pandas as pd

CSV_PATH = "carbon_footprint_calculator/initial_data/emission-factors" \
           "-transport.csv "


@lru_cache
def GetTransportData(csv_path=CSV_PATH):
    df = pd.read_csv(csv_path, header=0)
    return dict(zip(df["Means of transport"], df["Equivalent"]))

