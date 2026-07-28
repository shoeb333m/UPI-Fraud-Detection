import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier

# Load dataset
df = pd.read_csv("Dataset/PS_20174392719_1491204439457_log.csv")

# Target
y = df["isFraud"]

# Keep ONLY manual features
df = df[["type", "amount", "oldbalanceOrg", "newbalanceOrig"]]

# Encode type
le = LabelEncoder()
df["type"] = le.fit_transform(df["type"])

# Scale
scaler = StandardScaler()
X = scaler.fit_transform(df)

# Train model
model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X, y)

# Save
joblib.dump(model, "model/manual_fraud_model.pkl")
joblib.dump(scaler, "model/manual_scaler.pkl")
joblib.dump(le, "model/manual_type_encoder.pkl")

print("✅ Manual model trained")
