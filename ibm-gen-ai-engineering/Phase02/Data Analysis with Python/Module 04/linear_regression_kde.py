import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# Generating Sample Data
np.random.seed(42)
x = np.random.randn(100) * 10
y = 3 * x + np.random.normal(0, 3, 100) # Generate target variable with noise, linear relations
data = pd.DataFrame({'X': x, 'Y': y})

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    data[['X']], data['Y'], test_size=0.2, random_state=42
)

# Training a Model
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Plotting KDE for Observed vs Predicted Values
plt.figure(figsize=(8,5))
sns.kdeplot(y_test, label='Actual', fill=True, color='blue')
sns.kdeplot(y_pred, label='Predicted', fill=True, color='red')
plt.xlabel('Target Variables')
plt.ylabel('Density')
plt.title('KDE Comparison')
plt.legend()
os.makedirs('figures', exist_ok=True)
plt.savefig('figures/kde_comparison.png')
plt.show()
# Calculating Model Performance Metrics
mae = mean_absolute_error(y_test, y_pred)
print(f'Mean Absolute Error: {mae:.2f}')

# Display model coefficients
print(f'Coefficient: {model.coef_[0]:.2f}')
print(f'Intercept: {model.intercept_:.2f}')

# Calculating R² Score (Coefficient of Determination)
r2 = model.score(X_test, y_test)
print(f'R² Score: {r2:.2f}')