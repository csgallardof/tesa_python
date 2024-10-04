#libreria pandas 
#Permite tener una estructura bidimensional con la cual se puede manipular o almacener columnas 
# con gran volumen de datos. (x,y) herramienta poderosa

import pandas as pd
import numpy as np

file_path = 'monthly_sales.csv'
sales_data = pd.read_csv(file_path)
print(sales_data.head())


print("------------------")

data = np.array([[1,2,3],[4,7,10],[11,21,13]])
dt_from_array = pd.DataFrame(data, columns = ['A','B','C'])
print(dt_from_array)

print("------------------")

data1 = ([1, "Xavier" , 26], [2, 'Kevin' , 280], [3, "Miryan" , 40])
dt_from_list =pd.DataFrame(data1, columns=['id' , "Nombre",'Edad'])
print(dt_from_list)  