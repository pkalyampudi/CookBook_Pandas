
import pandas as pd

# Load dataset
df = pd.read_csv('health_data.csv', parse_dates=['AdmissionDate', 'DischargeDate'])

# Generate risk level summary
risk_counts = df['RiskLevel'].value_counts()

# Display risk summary
print(risk_counts)
