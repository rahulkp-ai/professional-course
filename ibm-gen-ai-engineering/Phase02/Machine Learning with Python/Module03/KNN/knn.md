# Supervised Learning with K-Nearest Neighbors (KNN)

## 1. Overview & Core Paradigm

- **Definition:** A supervised machine learning algorithm that utilizes a labeled dataset to assign labels or target values to new, unlabeled data points.
- **Dual Functionality:** Used for both **Classification** (discrete labels) and **Regression** (continuous values).
- **Core Paradigm:** Data points close to each other in feature space are considered "neighbors." The fundamental assumption is that points close to each other share similar features and tend to belong to the same class or have similar values.
- **Algorithm Type (Lazy Learner):**
  - Does not perform traditional model training or abstraction during a training phase.
  - Stores the training dataset in memory and performs computations on the fly when a query point is presented.
  - Still classified as supervised learning because it relies on known target labels and calculates query-to-training distances to make predictions.

---

## 2. Step-by-Step Algorithm Workflow

### Classification Process:

1. **Choose K:** Select a hyperparameter $K$ representing the number of neighbors to evaluate.
2. **Calculate Distance:** Compute the mathematical distance from the unlabeled query point to all labeled observations in the training data.
3. **Identify Neighbors:** Sort observations by distance and select the $K$ closest observations to the query point.
4. **Predict Class (Majority Vote):** Assign the query point the class label that occurs most frequently among its $K$ nearest neighbors.

### Regression Process:

- Perform steps 1–3 above, then predict the target value of the query point using the **average** or **median** of the target values of the $K$ nearest neighbors.

---

## 3. Practical Example & Model Evaluation (Iris Dataset)

- **Dataset Structure:** 150 total samples (50 each for _Iris setosa_, _Iris virginica_, and _Iris versicolor_).
- **Features:** Sepal length, sepal width, petal length, petal width (measured in centimeters).
- **Classification Example:** Using Scikit-Learn's `KNeighborsClassifier` with two input features (sepal length and petal length) and $K = 3$, the model generated decision boundaries achieving approximately **93% accuracy**.

### How to Tune $K$ (Optimal $K$ Search):

1. Split data into training and testing sets.
2. Set $K = 1$, fit the model on the training set, and calculate prediction accuracy on the test set.
3. Increment $K$ sequentially ($K = 2, 3, 4, \dots$).
4. Evaluate performance at each step and select the $K$ value yielding the highest test accuracy (e.g., $K = 4$ for the benchmark set).

---

## 4. Impact of Hyperparameter $K$

| $K$ Value       | Effect on Model                                  | Risk / Outcome        |
| :-------------- | :----------------------------------------------- | :-------------------- |
| **Small $K$**   | High sensitivity to local fluctuations and noise | **Overfitting**       |
| **Large $K$**   | Over-smoothing of local decision boundaries      | **Underfitting**      |
| **Optimal $K$** | Balanced tradeoff between bias and variance      | Best generalizability |

---

## 5. Key Challenges & Mitigation Strategies

### A. Skewed Class Distributions (Imbalanced Data)

- **Issue:** Dominant classes naturally appear more frequently among nearest neighbors, causing majority voting to favor the frequent class.
- **Solution:** Use **distance-weighted classification** (where closer neighbors exert greater influence on the vote than distant ones).

### B. Feature Scaling Discrepancies

- **Issue:** Features with larger numerical scales dominate distance calculations, distorting the relative importance of smaller-scaled features.
- **Solution:** Apply feature scaling techniques such as **Standardization** (or Normalization) prior to running KNN.

### C. Irrelevant & Redundant Features

- **Irrelevant Features:** Act as noise, requiring a larger $K$ to prevent overfitting, which increases computational complexity and degrades accuracy.
- **Redundant Features:** Increase distance-calculation workload without adding predictive value.
- **Solution:**
  - Utilize **domain knowledge** for feature selection.
  - Evaluate feature necessity by tuning $K$ with and without a specific feature and comparing performance metrics.
  - Keeping only relevant features lowers the required optimal $K$, improves model accuracy, and increases computational efficiency.
