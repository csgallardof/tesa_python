import pandas as pd
import numpy as np

file_path = 'monthly_sales.csv'
sales_data = pd.read_csv(file_path)
print(sales_data.head())