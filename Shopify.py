#Import library
import os
import csv
from pathlib import Path

import pandas as pd
import numpy as np

# Set path to collect data 
data = os.path.join('/Users/monalpayghan/Desktop/Shopify/data.csv')

# Make a reference to the election_data.csv file path
csv_path = data

# Set the name and path for file to output
file_to_output = "data_results.txt"

# Import the data set as a DataFrame
data_df = pd.read_csv(csv_path, encoding="utf-8")
data_df.head()

oa_sum = data_df['order_amount'].sum()
ti_sum = data_df['total_items'].sum()
print(oa_sum)
print(ti_sum)

AOV = oa_sum/ti_sum
AOV

print("%.2f" % AOV)

'${:,.2f}'.format(AOV)

# Incorrect calculation explained as a mistaken count() instead of sum() function
oa_sum = data_df['order_amount'].sum()
ti_count = data_df['total_items'].count()
AOV = oa_sum/ti_count
print(AOV)

