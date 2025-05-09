
import pandas as pd

# Load dataset
df = pd.read_csv('health_data.csv', parse_dates=['AdmissionDate', 'DischargeDate'])

# Flag critical patients
def is_critical(bp, hr):
    return bp > 140 or hr > 100

df['CriticalFlag'] = df.apply(lambda row: is_critical(row['BloodPressure'], row['HeartRate']), axis=1)

# Display result
print(df[['PatientID', 'BloodPressure', 'HeartRate', 'CriticalFlag']].head())
