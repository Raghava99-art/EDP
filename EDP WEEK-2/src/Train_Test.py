import pandas as pd
import numpy as np
df = pd.read_csv("healthcare_data.csv")
print("===== Healthcare Dataset =====")
print(df)
X = df["Blood_Pressure"]
Y = df["Medical_Cost"]
print("\nFeatures (Blood Pressure)")
print(X)
print("\nTarget (Medical Cost)")
print(Y)
split = int(len(df) * 0.8)
X_train = X[:split]
Y_train = Y[:split]
X_test = X[split:]
Y_test = Y[split:]
print("\n===== Training Data =====")
print(pd.DataFrame({
    "Blood Pressure": X_train.values,
    "Medical Cost": Y_train.values
}))
print("\n===== Testing Data =====")
print(pd.DataFrame({
    "Blood Pressure": X_test.values,
    "Medical Cost": Y_test.values
}))
mean_x = np.mean(X_train)
mean_y = np.mean(Y_train)
numerator = np.sum((X_train - mean_x) * (Y_train - mean_y))
denominator = np.sum((X_train - mean_x) ** 2)
m = numerator / denominator
c = mean_y - (m * mean_x)
print("\n===== Model Trained =====")
print("Slope (m):", round(m, 2))
print("Intercept (c):", round(c, 2))
print("\nRegression Equation")
print("Medical Cost = {:.2f} × Blood Pressure + {:.2f}".format(m, c))
predictions = m * X_test + c
print("\n===== Predictions =====")
results = pd.DataFrame({
    "Blood Pressure": X_test.values,
    "Actual Cost": Y_test.values,
    "Predicted Cost": np.round(predictions.values, 2)
})
print(results)
mae = np.mean(np.abs(Y_test - predictions))
mse = np.mean((Y_test - predictions) ** 2)
rmse = np.sqrt(mse)
print("\n===== Evaluation Metrics =====")
print("Mean Absolute Error (MAE):", round(mae, 2))
print("Mean Squared Error (MSE):", round(mse, 2))
print("Root Mean Squared Error (RMSE):", round(rmse, 2))