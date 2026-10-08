# Supervised Learning with Support Vector Machines (SVMs)

## Overview

Support Vector Machines (SVMs) are supervised learning algorithms used for both **classification** and **regression** tasks.

SVM works by mapping data instances into a multidimensional space where input features correspond to specific coordinates, and then finding an optimal **hyperplane** (decision boundary) that distinctly segregates classes.

---

## Key Concepts & Terminology

- **Hyperplane / Decision Boundary**: A boundary that segregates dataset classes.
  - In a 2D feature space, the decision boundary is a line.
  - In higher dimensions, it becomes a plane or hyperplane.
- **Margin**: The distance between the hyperplane and the closest data points from each class.
  - **Goal**: Maximize the margin. The larger the margin, the better the model's accuracy on new, unseen data.
- **Support Vectors**: The nearest data points from each class to the decision boundary. These points are fundamental to defining the hyperplane's location.
- **Mathematical Intuition (2D)**:
  - Given normalized data, the objective is to find weight vector $w$ and bias term $b$ such that $\|w\|$ is minimized, subject to $y_i(w^T x_i + b) \ge 1$.
  - **Decision Rule**: For an unknown point $x$, evaluate $w^T x + b$:
    - If $> 0$, the point belongs to Class 1 (above the line).
    - If $< 0$, the point belongs to Class 2 (below the line).

---

## Soft Margin & Parameter $C$

Real-world data is often noisy and overlapping, making perfect linear separation impossible.

- **Soft Margin**: Allows the model to tolerate a certain number of misclassifications while still maximizing the overall margin.
- **Parameter $C$**: Controls the trade-off between margin size and misclassification tolerance:
  - **Smaller $C$**: Allows more misclassifications $\rightarrow$ **Softer margin** (more tolerant, better generalization).
  - **Larger $C$**: Forces stricter separation $\rightarrow$ **Harder margin** (less tolerant).

---

## Kernel Trick (Non-Linear Classification)

When data is non-linearly separable in lower dimensions (e.g., concentric circles), SVM uses **kerneling** to map the data into a higher-dimensional space where a linear hyperplane can separate the classes.

### Scikit-Learn Kernel Functions

1. **Linear** (Default): Fits standard linear decision boundaries.
2. **Polynomial**: Uses polynomial features (e.g., parabolic embeddings) to separate complex shapes in higher dimensions.
3. **Radial Basis Function (RBF)**: Gives higher scores to points close to each other, decreasing exponentially with distance.
4. **Sigmoid**: Uses the same mathematical function as logistic regression.

---

## Support Vector Regression (SVR)

SVM can also be adapted to continuous target variables using **Support Vector Regression (SVR)**:

- **$\epsilon$-Tube (Epsilon Margin)**: Defines a margin/buffer around the predicted continuous curve.
  - **Inside $\epsilon$-tube**: Interpreted as valid signal.
  - **Outside $\epsilon$-tube**: Interpreted as noise.
- Increasing $\epsilon$ widens the margin around the prediction curve.

---

## Advantages & Limitations

### Advantages

- Highly effective in high-dimensional spaces.
- Robust to overfitting (especially with appropriate regularization).
- Excels on linearly separable and weakly separable data (via soft margin).

### Limitations

- Slow training performance on large datasets.
- Sensitive to noise and overlapping classes.
- Non-trivial to choose and tune kernel functions and parameters ($C$, $\epsilon$).

---

## Common Applications

- **Computer Vision**: Image classification, handwritten digit recognition.
- **Natural Language Processing**: Text parsing, spam detection, sentiment analysis.
- **General Machine Learning**: Speech recognition, anomaly detection, noise filtering.
