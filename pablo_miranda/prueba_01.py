
import pandas as pd

print("Registration Report")

file_path = 'Prueba 1 Tesa.csv'
registration_data = pd.read_csv(file_path, sep=';', on_bad_lines='skip', skiprows=5, header=0, parse_dates=False)

print("\nCountries")
countries = registration_data.groupby('Country/Region').size()
print(countries)

approval_status = registration_data.groupby('Approval Status')
#print(approval_status.first())

approved_count = registration_data['Approval Status'].value_counts()['approved']
print('\nCountries with approved status: ' + str(approved_count))
