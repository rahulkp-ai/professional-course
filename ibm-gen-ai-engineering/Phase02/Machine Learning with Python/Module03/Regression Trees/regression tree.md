# Regression Trees

A **regression tree** is a variant of a decision tree adapted to predict continuous target variables rather than discrete categorical labels.

---

## Classification vs. Regression Trees

| Feature                  | Classification Tree                             | Regression Tree                                            |
| ------------------------ | ----------------------------------------------- | ---------------------------------------------------------- |
| **Target Variable**      | Categorical (e.g., True/False, Spam/Not Spam)   | Continuous / Floating (e.g., Salary, Temperature)          |
| **Leaf Prediction**      | Majority vote of target classes                 | Average ($\hat{y}$) or Median of target values             |
| **Split Quality Metric** | Entropy / Information Gain                      | Mean Squared Error (MSE) / Variance Reduction              |
| **Use Cases**            | Image classification, spam detection, diagnosis | Revenue forecasting, wildfire risk, temperature prediction |

---

## Node Predictions ($\hat{y}$)

- **Mean (Default):** Calculated as the average of actual target values $y_i$ in the node:

$$\hat{y} = \frac{1}{N} \sum_{i=1}^{N} y_i$$

- **Median:** Preferred when the data distribution is skewed (more robust to outliers), though computationally more expensive than the mean.

---

## Measuring Split Quality (MSE)

Regression trees select features and thresholds that minimize the target variance (error) within the resulting child nodes.

### Weighted MSE Calculation

For a candidate split dividing a dataset into left ($L$) and right ($R$) nodes:

$$\text{MSE}_{\text{weighted}} = \frac{1}{N_{\text{total}}} \left( N_L \cdot \text{MSE}_L + N_R \cdot \text{MSE}_R \right)$$

- **Goal:** Minimize $\text{MSE}_{\text{weighted}}$. Lower values indicate lower target variance and higher split quality.

---

## Handling Feature Types for Splits

### 1. Binary Features

Split directly by the two categorical values. The weighted MSE has only one outcome, so it is inherently optimized.

### 2. Multi-Class Categorical Features

Use strategies like **One-vs-One** or **One-vs-All** to form candidate binary splits, then pick the split yielding the lowest weighted MSE.

### 3. Continuous Features (Threshold Selection Strategy)

1. Sort feature values in ascending order ($X_i \le X_j$).
2. Remove duplicate values ($X_i < X_j$).
3. Generate candidate thresholds ($\alpha_i$) as midpoints between consecutive sorted values:

$$\alpha_i = \frac{X_i + X_{i+1}}{2}$$

4. Evaluate every $\alpha_i$ and select the threshold that minimizes weighted MSE.

> **Efficiency Note:** Exhaustive midpoint search does not scale well to massive datasets. For large data, sample a sparse subset of candidate thresholds (considering target distribution) to trade slight accuracy for faster execution.
