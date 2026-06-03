import numpy as np
import time
from sklearn.metrics import mean_squared_error, r2_score

def run_normal_equation(
    X_train_bias,
    X_test_bias,
    y_train,
    y_test
):
    print("\n--- Running Normal Equation ---")

    start_time = time.time()

    theta_normal = (
        np.linalg.inv(X_train_bias.T @ X_train_bias)
        @ X_train_bias.T
        @ y_train
    )

    train_time = time.time() - start_time

    start_time = time.time()

    y_pred = X_test_bias @ theta_normal

    pred_time = time.time() - start_time

    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"MSE: {mse:.4f}")
    print(f"R²: {r2:.4f}")

    return {
        "theta": theta_normal,
        "mse": mse,
        "r2": r2,
        "train_time": train_time,
        "prediction_time": pred_time
    }