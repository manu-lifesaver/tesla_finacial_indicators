Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
# Using pandas to read the csv file.
import pandas as pd
# Creating a DataFrame from the csv file
tesla_bs = pd.read_csv (".../Tesla_Balance_Sheet.csv")
# Creating current assets DataFrame 
ca_df = tesla_bs.loc[tesla_bs["Account"] == "Current Assets"]
# Creating current liabilities DataFrame
cl_df = tesla_bs.loc[tesla_bs["Account"] == "Current Liabilities"]
# Converting DataFrames to lists
ca_list = ca_df.values.tolist()
cl_list = cl_df.values.tolist()
# Selecting 2021 values and converting them to integers
ca_2021 = int(ca_list[0][1])
cl_2021 = int(cl_list[0][1])
#  Calculating working capital for the year 2021
#(working capital = current assets - current liabilities)
wc_2021 = ca_2021 - cl_2021
print(wc_2021)
