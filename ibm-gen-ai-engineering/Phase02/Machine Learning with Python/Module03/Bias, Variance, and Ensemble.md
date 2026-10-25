# Bias, Variance, and Ensemble Models - Study

## 1. Core Concepts: Bias vs. Variance

- **Bias (Accuracy):**
  - Definition: How on-target or off-target a model's predictions are (measured by the average difference between predicted and actual target values).
  - Dart Board Analogy: Grouping darts near the center indicates **low bias** (high accuracy); boards further away show **high bias**.
  - A perfect predictor has **zero bias**.
- **Variance (Precision):**
  - Definition: How much a model's predictions fluctuate when trained on different subsets of the same dataset (represents precision and sensitivity to training data).
  - Dart Board Analogy: Darts spread out indicate **high variance**; darts grouped closely together show **low variance**.
  - Achieving high scores/generalization requires both **low bias** and **low variance**.

---

## 2. Quantitative & Visualizing Metrics

- **Prediction Bias Example:**
  - Linear OLS fit for blue data points has a bias of `0.22`.
  - Same model shifted down by 4 units has a much higher bias of `4.22`.
- **Prediction Variance Example:**
  - High variance makes a model overly sensitive, causing it to **overfit** training data and track noise or outliers.
  - Models with low prediction variance generalize well to unseen data and are less sensitive to noise.

---

## 3. The Bias-Variance Tradeoff

- **Model Complexity Impact:**
  - As complexity **increases**: Bias (blue curve) **declines**, while variance (green curve) **rises**.
  - **Low Complexity:** Leads to high bias $\rightarrow$ poor predictions even on training data (**underfitting**).
  - **High Complexity:** Leads to high variance $\rightarrow$ sensitive to training data, poor on unseen data (**overfitting**).
  - **Crossover Point:** The optimal complexity sweet spot where generalization error is minimized (though random noise/generalization error can never be completely eliminated).

---

## 4. Weak vs. Strong Learners

- **Weak Learners:**
  - Supervised ML models performing slightly better than random guessing.
  - Characterized by **high bias and low variance** (tends to **underfit**).
- **Strong Learners:**
  - Characterized by **low bias and high variance** (tends to **overfit**).

---

## 5. Ensemble Methods: Bagging vs. Boosting

### Base Learners

- Decision or regression trees are commonly used because their bias and variance can be easily adjusted by altering their depth.

### A. Bagging (Bootstrap Aggregating)

- **Mechanism:** Repeatedly trains base learners (high variance, low bias, e.g., shallow decision trees) in **parallel** on bootstrapped subsets of data and averages their predictions.
- **Outcome:** Significantly **reduces prediction variance** and lowers the risk of overfitting.
- **Key Example:** **Random Forests** (trains multiple decision trees on bootstrapped datasets; aggregation minimizes high prediction variance with only a slight increase in bias).

### B. Boosting

- **Mechanism:** Builds a series of weak learners (low variance, high bias) **sequentially**, with each new model aiming to correct the errors/residuals of the previous one.
- **Outcome:** Systematically reduces prediction error, lowering **prediction bias** and mitigating underfitting.
- **Process Details:** Weights of misclassified data from previous iterations are increased; weights of correctly classified data are decreased.
- **Popular Algorithms:** Gradient Boosting, XGBoost, and AdaBoost.

---

## 6. Summary Comparison Table

| Ensemble Method | Primary Goal          | Base Learners           | Training Type                           | Main Target Mitigated |
| :-------------- | :-------------------- | :---------------------- | :-------------------------------------- | :-------------------- |
| **Bagging**     | Mitigate overfitting  | High variance, Low bias | Parallel (Bootstrapped samples)         | Reduces **Variance**  |
| **Boosting**    | Mitigate underfitting | Low variance, High bias | Sequential (Iterative error correction) | Reduces **Bias**      |
