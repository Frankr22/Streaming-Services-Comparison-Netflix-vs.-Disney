import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

disney_path = "Data/disney_plus_titles.csv"
disney_file = pd.read_csv(disney_path)


# reduced_file = disney_file.dropna(how='any')
reduced_file = disney_file.drop_duplicates(subset="title")

# check type
type_gb = reduced_file.groupby("type").count()
