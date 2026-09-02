## Model Evaluation

The developed models will be evaluated using a held-out test dataset.

### Mean Absolute Error (MAE)

Measures the average absolute difference between actual and predicted insurance charges. Lower MAE indicates better prediction performance.

$$\text{MAE} = \frac{1}{n} \sum_{i=1}^{n} \vert{}y_i - \hat{y}_i\vert{}$$

---

### Mean Squared Error (MSE)

Measures the average squared difference between actual and predicted values. Lower MSE indicates better performance.

$$\text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2$$

---

### Root Mean Squared Error (RMSE)

RMSE is the square root of MSE and expresses prediction error in the same unit as the target variable ($). Lower RMSE indicates better prediction performance.

$$\text{RMSE} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2}$$

---

### R² Score (Coefficient of Determination)

$R^2$ measures the proportion of variance in insurance charges explained by the model. A higher $R^2$ value generally indicates better explanatory performance.

$$R^2 = 1 - \frac{\sum_{i=1}^{n} (y_i - \hat{y}_i)^2}{\sum_{i=1}^{n} (y_i - \bar{y})^2}$$

_Where $n$ is the sample size, $y_i$ is the actual value, $\hat{y}_i$ is the predicted value, and $\bar{y}$ is the mean of the actual target values._
