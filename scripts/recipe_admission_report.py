
import pandas as pd

# Load dataset
df = pd.read_csv('health_data.csv', parse_dates=['AdmissionDate', 'DischargeDate'])

# Generate weekly admission report
df['Week'] = df['AdmissionDate'].dt.isocalendar().week
weekly_admissions = df.groupby('Week').size()

# Display report
print(weekly_admissions)
