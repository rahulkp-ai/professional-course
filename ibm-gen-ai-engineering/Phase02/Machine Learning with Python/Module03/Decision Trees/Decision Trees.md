# Decision Trees for Machine Learning

## 1. What is a Decision Tree?

A **Decision Tree** is a supervised machine learning algorithm visualized as a flowchart used for classifying data points.

- **Internal Node:** Represents a test on an attribute/feature.
- **Branch:** Represents the outcome/result of the test.
- **Leaf Node (Terminal Node):** Assigns the final class label or outcome.

---

## 2. Example: Drug Prescription Model

- **Dataset Features:** Age (Young, Middle-aged, Senior), Gender (Male, Female), Blood Pressure, Cholesterol (Normal, High).
- **Target Variable:** Drug response (Drug A vs. Drug B).
- **Logic:**
- **Drug B** is prescribed if:
- Patient is Middle-aged.
- Patient is Young AND Male.
- Patient is Senior AND has Normal Cholesterol.

- **Drug A** is prescribed if:
- Patient is Young AND Female.
- Patient is Senior AND has High Cholesterol.

---

## 3. Tree Building & Recursive Partitioning

Trees are built via **recursive partitioning** by considering dataset features one by one:

1. Start with a root node containing labeled training data.
2. Select the feature that best splits the data into pre-labeled classes.
3. Partition the data along branches to new nodes.
4. Repeat the splitting process recursively using unused features until a stopping point is reached.

---

## 4. Tree Pruning & Stopping Criteria

Pruning prevents **overfitting** (capturing noise and irrelevant details in overly complex trees), improves predictive accuracy, and ensures better generalization.

### Pre-emptive Stopping Criteria

Growth stops when:

- Maximum tree depth is reached.
- Minimum number of data points in a node is reached/exceeded.
- Minimum number of samples in a leaf node is reached/exceeded.
- Maximum number of leaf nodes is reached.
- All data points in a node belong to a single class (pure node).

### Post-Pruning

Branches that do not significantly improve system performance are cut after growth.

---

## 5. Splitting Criteria & Impurity Measures

To determine the best feature for a split, the algorithm evaluates how well a feature decreases impurity across classes.

### A. Entropy

Measures information disorder or randomness/uncertainty within a node.

- **Homogeneous Node (Pure):** $\text{Entropy} = 0$
- **Equally Divided Node (Impure):** $\text{Entropy} = 1$
- **Formula:**

$$H(S) = -p_A \log_2(p_A) - p_B \log_2(p_B)$$

_(where $p_A$ and $p_B$ are class proportions)_

### B. Information Gain

Calculated as the entropy before the split minus the weighted average entropy after splitting on a feature:

$$\text{Information Gain} = \text{Entropy}_{\text{before}} - \text{Entropy}_{\text{after}}$$

- **Goal:** Maximize Information Gain (find features that minimize entropy).

### C. Gini Impurity

An alternative split criterion used to measure split quality.

---

## 6. Key Advantages of Decision Trees

- **High Interpretability:** Highly visual structure makes decision-making transparent.
- **Feature Importance:** Step-by-step feature selection offers insights into which attributes are most predictive.
