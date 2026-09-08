import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# ==========================================
# 1. Data Acquisition & Initial Exploration
# ==========================================

# Load fuel consumption dataset from IBM Cloud Object Storage
DATASET_URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%202/data/FuelConsumptionCo2.csv"
df = pd.read_csv(DATASET_URL)

# Inspect a random sample and compute descriptive summary statistics
print("Sample Record:\n", df.sample())
print("\nDescriptive Statistics:\n", df.describe())

# ==========================================
# 2. Feature Selection & Subset Extraction
# ==========================================

# Extract target variable (CO2EMISSIONS) and candidate predictor features
selected_features = ['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_COMB', 'CO2EMISSIONS']
cdf = df[selected_features]
print("\nSelected Features Sample:\n", cdf.sample(9))

# ==========================================
# 3. Exploratory Data Analysis (EDA)
# ==========================================

# Plot distributions for all selected features
cdf.hist()
plt.tight_layout()
plt.show()

# Evaluate bivariate linear relationship: Combined Fuel Consumption vs CO2 Emissions
plt.scatter(cdf.FUELCONSUMPTION_COMB, cdf.CO2EMISSIONS, color='blue', alpha=0.6)
plt.xlabel("Combined Fuel Consumption (L/100km)")
plt.ylabel("CO2 Emissions (g/km)")
plt.title("Fuel Consumption vs CO2 Emissions")
plt.show()

# Evaluate bivariate linear relationship: Engine Size vs CO2 Emissions
plt.scatter(cdf.ENGINESIZE, cdf.CO2EMISSIONS, color='blue', alpha=0.6)
plt.xlabel("Engine Size (L)")
plt.ylabel("CO2 Emissions (g/km)")
plt.xlim(0, 27)  # Set visual limits for engine size range
plt.title("Engine Size vs CO2 Emissions")
plt.show()

# Evaluate bivariate linear relationship: Cylinders vs CO2 Emissions
plt.scatter(cdf.CYLINDERS, cdf.CO2EMISSIONS, color='blue', alpha=0.6)
plt.xlabel("Number of Cylinders")
plt.ylabel("CO2 Emissions (g/km)")
plt.title("Cylinders vs CO2 Emissions")
plt.show()

# ==========================================
# 4. Data Preprocessing & Partitioning
# ==========================================

# Extract feature (X) and target label (y) as NumPy arrays
X = cdf['ENGINESIZE'].to_numpy()
y = cdf['CO2EMISSIONS'].to_numpy()

# Perform an 80/20 train-test split for unbiased model evaluation
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42
)
print(f"\nTraining set array type: {type(X_train)}, Shape: {X_train.shape}")

# ==========================================
# 5. Model Initialization & Training
# ==========================================

# Instantiate and fit the Ordinary Least Squares (OLS) Linear Regression model
regressor = LinearRegression()

# Reshape 1D feature vectors into 2D matrices required by scikit-learn (N_samples, N_features)
X_train_2d = X_train.reshape(-1, 1)
X_test_2d = X_test.reshape(-1, 1)

regressor.fit(X_train_2d, y_train)

# Output learned model parameters
print(f"\nModel Slope (Coefficient): {regressor.coef_[0]:.4f}")
print(f"Model Y-Intercept: {regressor.intercept_:.4f}")

# ==========================================
# 6. Training Visualization
# ==========================================

# Overlay the fitted regression line against training data observations
plt.scatter(X_train, y_train, color='blue', alpha=0.5, label='Training Data')
plt.plot(X_train, regressor.coef_[0] * X_train + regressor.intercept_, '-r', label='Fitted Line')
plt.xlabel('Engine Size (L)')
plt.ylabel('CO2 Emissions (g/km)')
plt.title('Simple Linear Regression Fit')
plt.legend()
plt.show()

# ==========================================
# 7. Out-of-Sample Performance Evaluation
# ==========================================

# Generate predictions on the unseen test set
y_pred = regressor.predict(X_test_2d)

# Calculate standard regression performance metrics
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print(f"\nMean Absolute Error (MAE): {mae:.2f}")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
print(f"R² Score: {r2:.2f}")