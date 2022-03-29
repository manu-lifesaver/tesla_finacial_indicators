Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
# Using pandas to read the csv file.
import pandas as pd
# Creating a DataFrame from the csv file
tesla_bs = pd.read_csv ("path/to/Tesla_Balance_Sheet.csv")
# Setting Account column as the index
tesla_ind = tesla_bs.index("Account")
