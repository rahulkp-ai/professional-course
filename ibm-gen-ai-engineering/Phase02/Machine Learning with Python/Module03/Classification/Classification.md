# Classification in Supervised Machine Learning

## 1. Overview & Core Concepts

- **Definition:** Classification is a **supervised machine learning (ML)** method that uses fully trained models to predict categorical labels (discrete values) for new, unseen data.
- **Goal:** Understand data in the correct context to answer specific questions accurately.
- **Workflow:** Input data is adjusted to fit the algorithm, defining the relationship between input features and predicted target labels.

---

## 2. Common Applications & Use Cases

### General Applications

- Email filtering
- Speech-to-text conversion
- Handwriting recognition
- Biometric identification
- Document classification

### Business & Marketing Use Cases

- **Churn Prediction:** Predicts whether a customer will discontinue a service.
- **Customer Segmentation:** Predicts the specific category to which a customer belongs.
- **Campaign Response:** Predicts whether a customer is likely to respond to an ad campaign.

### Practical Examples

- **Binary Classification (Loan Default):** A bank uses historical default data (age, income, credit debt) to predict whether a new applicant will default (**Default** vs. **No Default**).
- **Multi-Class Classification (Drug Prescription):** Predicts which medication out of three or more options is appropriate for a patient based on historical treatment response data.

---

## 3. Classification Algorithms

Common machine learning classification algorithms include:

- Naive Bayes
- Logistic Regression
- Decision Trees
- K-Nearest Neighbors (KNN)
- Support Vector Machines (SVM)
- Neural Networks

> **Note:** Algorithms like Logistic Regression, KNN, and Decision Trees can natively distinguish multiple classes. Algorithms strictly limited to binary classification require specific strategies to handle multi-class problems.

---

## 4. Multi-Class Prediction Strategies

### A. One-Versus-All (One-vs-Rest / OvA)

- **Concept:** Implements a set of independent binary classifiers—exactly **$k$ binary classifiers** for $k$ target classes.
- **Mechanism:** Each classifier focuses on a single class vs. all remaining classes.
- **Outlier Detection:** Points not picked up by any classifier fall into an unclassified/outlier group, making OvA useful for identifying noise or anomalies.

### B. One-Versus-One (OvO)

- **Concept:** Trains a binary classifier for **every possible pair of classes** using only the subset of data corresponding to those two labels.
- **Question Asked:** Shifts the evaluation from _"Is it Class A?"_ to _"Is it Class A or Class B?"_
- **Voting Mechanisms:**
- **Popularity Voting (Majority Vote):** The class predicted by the most binary classifiers wins.
- **Weighted Voting (Tie-Breaking):** In case of a tie, votes are weighted by the confidence level or probability assigned by each classifier. Alternatively, switch to a One-Versus-All approach.
