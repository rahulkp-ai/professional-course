# Model Development

## Overview

Model development is the process of creating a mathematical model that predicts a target value using one or more input features. In this context, the objective is to **predict the price of a used car** from various vehicle characteristics.

---

# Learning Objectives

After completing this topic, you should understand:

- Simple Linear Regression
- Multiple Linear Regression
- Model Evaluation using Visualization
- Polynomial Regression
- Pipelines
- R-squared (R²)
- Mean Squared Error (MSE)
- Prediction and Decision Making
- Determining the Fair Value of a Used Car

---

# What is a Model?

A **model** (or **estimator**) is a mathematical equation that predicts an output based on one or more input variables.

### Components

- **Independent Variables (Features)** → Input variables used for prediction.
- **Dependent Variable (Target)** → Output variable that the model predicts.

### Example

**Feature (Input):**

- Highway Miles Per Gallon (Highway MPG)

**Target (Output):**

- Car Price

```
Highway MPG  ─────►  Model  ─────►  Predicted Price
```

---

# Importance of More Features

Generally,

> **More relevant data (features) leads to better predictions.**

Instead of using only one feature, we can use multiple features such as:

- Engine Size
- Horsepower
- Curb Weight
- Highway MPG
- City MPG
- Number of Cylinders
- Drive Wheels
- Fuel Type

The model combines these variables to produce a more accurate estimate of the car's price.

```
Engine Size ─┐
Horsepower ──┤
Weight ──────┤
MPG ─────────┤
Fuel Type ───┤
             ▼
        Machine Learning Model
             ▼
      Predicted Car Price
```

---

# Why More Data Matters

Consider two nearly identical cars:

| Car   | Color |
| ----- | ----- |
| Car A | Red   |
| Car B | Pink  |

Suppose **pink cars consistently sell for lower prices**.

If the model only uses:

- Horsepower
- Engine Size
- Mileage

and **does not include Color**, then both cars receive the **same predicted price**, even though their actual market values differ.

### Lesson

A model can only learn patterns from the <b>information</b> you provide.

If an important feature is missing, prediction accuracy decreases.

---

# Choosing Different Models

Improving predictions is not only about collecting more data.

You can also improve performance by selecting a better model.

In this course, the following regression models are introduced:

## 1. Simple Linear Regression

Uses **one independent variable** to predict the target.

```
One Feature
     │
     ▼
Simple Linear Regression
     ▼
Predicted Price
```

---

## 2. Multiple Linear Regression

Uses **multiple independent variables** simultaneously.

```
Feature 1 ─┐
Feature 2 ─┤
Feature 3 ─┤
Feature n ─┘
      │
      ▼
Multiple Linear Regression
      ▼
Predicted Price
```

---

## 3. Polynomial Regression

Captures **non-linear relationships** between features and the target by fitting a curve rather than a straight line.

Useful when data does not follow a simple linear pattern.

---

# Key Takeaways

- A model predicts a target variable from one or more input features.
- Features are also called **independent variables**.
- The predicted value is the **dependent variable**.
- More **relevant** features generally improve prediction accuracy.
- Missing important features can reduce model performance.
- Different regression models are suited for different relationships in the data.
- The course covers:
  - Simple Linear Regression
  - Multiple Linear Regression
  - Polynomial Regression
  - Model Evaluation (Visualization, R², MSE)
  - Pipelines
  - Prediction and Decision Making

---

# Summary

Model development is the foundation of predictive analytics. By selecting meaningful features and an appropriate regression model, we can estimate the fair market value of a used car with greater accuracy. Both **data quality** and **model selection** play critical roles in building reliable predictive models.
