import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# ==========================================
# 1. Data Acquisition & Initial Exploration
# ==========================================

# Load fuel consumption dataset from IBM Cloud Object Storage
DATASET_URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%202/data/FuelConsumptionCo2.csv"
df = pd.read_csv(DATASET_URL)

print("Sample Record:\n", df.sample())
print("\nDescriptive Statistics:\n", df.describe())

# ==========================================
# 2. Feature Selection & Correlation Analysis
# ==========================================

# Drop non-numeric categorical attributes to prepare for correlation computation
categorical_cols = ['MODELYEAR', 'MAKE', 'MODEL', 'VEHICLECLASS', 'TRANSMISSION', 'FUELTYPE']
df = df.drop(columns=categorical_cols)

# Display pairwise feature correlations
print("\nFeature Correlation Matrix:\n", df.corr())

# Retain only primary predictor variables and target variable (CO2EMISSIONS)
cols_to_drop = ['CYLINDERS', 'FUELCONSUMPTION_CITY', 'FUELCONSUMPTION_HWY', 'FUELCONSUMPTION_COMB']
df = df.drop(columns=cols_to_drop)

print("\nProcessed Features Head:\n", df.head(9))

# ==========================================
# 3. Exploratory Visualization (Scatter Matrix)
# ==========================================

# Plot pairwise feature relationships using a scatter matrix
axes = pd.plotting.scatter_matrix(df, alpha=0.3, figsize=(10, 10), diagonal='kde')

# Rotate axis labels for visual clarity
for ax in axes.flatten():
    ax.xaxis.label.set_rotation(90)
    ax.yaxis.label.set_rotation(0)
    ax.yaxis.label.set_ha('right')

plt.tight_layout()
plt.gcf().subplots_adjust(wspace=0.1, hspace=0.1)
plt.show()

# ==========================================
# 4. Feature Standardization & Data Partitioning
# ==========================================

# Separate input predictors (X) and target variable (y)
X = df[['ENGINESIZE', 'FUELCONSUMPTION_COMB_MPG']].to_numpy()
y = df['CO2EMISSIONS'].to_numpy()

# Standardize predictors (Z-score normalization: zero mean, unit variance)
std_scaler = StandardScaler()
X_std = std_scaler.fit_transform(X)

print("\nStandardized Features Summary:\n", pd.DataFrame(X_std).describe().round(2))

# Perform an 80/20 train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X_std, y, test_size=0.20, random_state=42
)

# ==========================================
# 5. Multiple Linear Regression Training
# ==========================================

# Instantiate and fit Ordinary Least Squares (OLS) Multiple Linear Regression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Extract learned standardization space parameters
coef_scaled = regressor.coef_
intercept_scaled = regressor.intercept_

print(f"\nScaled Feature Coefficients: {coef_scaled}")
print(f"Scaled Feature Intercept: {intercept_scaled:.4f}")

# ==========================================
# 6. Parameter De-standardization (Original Space)
# ==========================================

# Extract scaler parameters (mean and standard deviation)
scaler_means = std_scaler.mean_
scaler_stds = np.sqrt(std_scaler.var_)

# Mathematically map coefficients back to the unstandardized metric space
# Formula: w_orig = w_scaled / sigma ; b_orig = b_scaled - sum(w_scaled * mu / sigma)
coef_original = coef_scaled / scaler_stds
intercept_original = intercept_scaled - np.sum((scaler_means * coef_scaled) / scaler_stds)

print(f"\nOriginal Feature Coefficients: {coef_original}")
print(f"Original Feature Intercept: {intercept_original:.4f}")

# ==========================================
# 7. Model Evaluation & Metrics
# ==========================================

y_pred = regressor.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print(f"\nModel Evaluation Metrics (Test Set):")
print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
print(f"R² Score: {r2:.2f}")

# ==========================================
# 8. 3D Decision Surface Visualization
# ==========================================

# Extract test features for 3D coordinate space
X1_test = X_test[:, 0]  # Standardized Engine Size
X2_test = X_test[:, 1]  # Standardized Fuel Consumption MPG

# Generate surface grid for the fitted 3D plane
x1_grid = np.linspace(X1_test.min(), X1_test.max(), 100)
x2_grid = np.linspace(X2_test.min(), X2_test.max(), 100)
x1_surf, x2_surf = np.meshgrid(x1_grid, x2_grid)

# Compute hyperplane z-values (predictions across grid points)
y_surf = intercept_scaled + (coef_scaled[0] * x1_surf) + (coef_scaled[1] * x2_surf)

# Partition actual data points relative to the regression plane (residuals check)
above_plane = y_test >= y_pred
below_plane = y_test < y_pred

# Render 3D regression visual
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Scatter points colored by position relative to prediction surface
ax.scatter(X1_test[above_plane], X2_test[above_plane], y_test[above_plane], 
           color='blue', label="Above Plane", s=50, alpha=0.7, edgecolors='k')
ax.scatter(X1_test[below_plane], X2_test[below_plane], y_test[below_plane], 
           color='orange', label="Below Plane", s=30, alpha=0.4, edgecolors='k')

# Render hyperplane mesh
ax.plot_surface(x1_surf, x2_surf, y_surf, color='gray', alpha=0.3)

# Configure plot axes and metadata
ax.view_init(elev=15, azim=45)
ax.set_xlabel('Engine Size (Standardized)', fontsize=10)
ax.set_ylabel('Fuel Consumption MPG (Standardized)', fontsize=10)
ax.set_zlabel('CO2 Emissions (g/km)', fontsize=10)
ax.set_title('Multiple Linear Regression Hyperplane Fit', fontsize=14)
ax.legend(loc='upper right')
plt.tight_layout()
plt.show()

# ==========================================
# 9. Component Feature Marginal Visualizations
# ==========================================

# Marginal Plot 1: Standardized Engine Size vs CO2 Emissions
plt.figure(figsize=(8, 4))
plt.scatter(X_train[:, 0], y_train, color='blue', alpha=0.4, label='Training Samples')
plt.plot(X_train[:, 0], coef_scaled[0] * X_train[:, 0] + intercept_scaled, '-r', label='Partial Fit')
plt.xlabel("Engine Size (Standardized)")
plt.ylabel("CO2 Emissions (g/km)")
plt.title("Marginal Effect: Engine Size")
plt.legend()
plt.show()

# Marginal Plot 2: Standardized Fuel Consumption MPG vs CO2 Emissions
plt.figure(figsize=(8, 4))
plt.scatter(X_train[:, 1], y_train, color='blue', alpha=0.4, label='Training Samples')
plt.plot(X_train[:, 1], coef_scaled[1] * X_train[:, 1] + intercept_scaled, '-r', label='Partial Fit')
plt.xlabel("Fuel Consumption MPG (Standardized)")
plt.ylabel("CO2 Emissions (g/km)")
plt.title("Marginal Effect: Fuel Consumption (MPG)")
plt.legend()
plt.show()