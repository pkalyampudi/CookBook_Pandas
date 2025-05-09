
import pandas as pd

# Load dataset
df = pd.read_csv('.../Pandas Cookbook/Chapter 2/data/health_data.csv', parse_dates=['AdmissionDate', 'DischargeDate'])

# Define custom scoring function
def custom_score(row):
    score = row['BloodPressure'] * 0.3 + row['HeartRate'] * 0.7
    return round(score, 2)

# Apply scoring function
df['HealthScore'] = df.apply(custom_score, axis=1)

# Display result
print(df[['PatientID', 'HealthScore']].head())
