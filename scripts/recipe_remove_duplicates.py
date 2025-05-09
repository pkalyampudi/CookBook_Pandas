
import pandas as pd

# Load dataset
df = pd.read_csv('health_data.csv', parse_dates=['AdmissionDate', 'DischargeDate'])

# Remove duplicate records based on PatientID
df.drop_duplicates(subset=['PatientID'], inplace=True)

# Display result
print(df.head())
