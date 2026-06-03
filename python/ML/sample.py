import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score

# 1. Load the dataset
# Replace 'air_quality_data.csv' with your specific file path if it differs
data_path = "/Users/m1pro/Downloads/air_quality_data.xlsx"
df = pd.read_excel(data_path)

print("Dataset Shape:", df.shape)
print(df.head())

# 2. Select Features and Target
# Using chemical features to predict PM2.5 concentrations
features = ['co', 'no', 'no2', 'o3', 'so2', 'pm10', 'nh3']
target = 'pm2_5'

X = df[features].values
y = df[target].values

# 3. Train-Test Split (80% Train, 20% Test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Feature Scaling (Crucial for Gradient Descent convergence)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 5. Add Bias/Intercept Term (Column of 1s) to the matrices
X_train_bias = np.c_[np.ones(X_train_scaled.shape[0]), X_train_scaled]
X_test_bias = np.c_[np.ones(X_test_scaled.shape[0]), X_test_scaled]

# Dictionary to hold benchmarking metrics
results = {}
print("\nData preparation complete!")