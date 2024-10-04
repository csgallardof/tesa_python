import pandas as pd
import numpy as np

file_path ='monthly_sales.csv'
sales_data= pd.read_csv(file_path)
print(sales_data.head())

print("----------------")
data = np.array([[1,2,3],[4,7,10],[11,21,13]])
dt_from_array= pd.DataFrame(data, columns=['A','B','C'])
print (dt_from_array)

print("----------------")
data_01=[[1,'Edwin',22],[2,'Leonardo',45],[3,'Diana',35]]
df_from_list=pd.DataFrame(data_01,columns=['A','B','C'])
print (df_from_list)

print (df_from_list)