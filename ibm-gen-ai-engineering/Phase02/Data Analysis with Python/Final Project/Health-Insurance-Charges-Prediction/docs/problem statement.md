# Health Insurance Charges Prediction Using Machine Learning

## 1. Project Title

**Health Insurance Charges Prediction Using Machine Learning**

---

## 2. Problem Statement

Healthcare and health insurance costs vary significantly among individuals due to several demographic, lifestyle, and health-related factors. Accurately estimating an individual's medical insurance charges can help insurance providers improve pricing strategies, risk assessment, and decision-making.

This project aims to develop a **machine learning-based regression system** capable of predicting the annual health insurance charges of an individual using demographic, health, lifestyle, and geographic attributes.

The system will analyze factors such as **age, gender, Body Mass Index (BMI), number of children, smoking status, and region** to determine their relationship with insurance charges. Exploratory Data Analysis (EDA) will be performed to identify the attributes that have the greatest influence on insurance costs.

Multiple regression approaches, including **Simple Linear Regression, Multiple Linear Regression, and Ridge Regression**, will then be developed and evaluated to determine an appropriate model for predicting insurance charges.

The project ultimately aims to demonstrate how machine learning can be applied to transform individual-level health and demographic information into an estimated insurance cost.

---

## 3. Project Aim

The primary aim of this project is to:

> **Design and evaluate a machine learning-based regression system that predicts health insurance charges from demographic, health, lifestyle, and geographical attributes.**

---

## 4. Dataset Description

The dataset contains information about individuals and their corresponding health insurance charges.

Each record represents an insured individual, while the attributes describe their demographic characteristics, health-related information, lifestyle factors, geographical region, and insurance cost.

### 4.1 Dataset Parameters

| Parameter        | Description                                              | Data Type                     |
| ---------------- | -------------------------------------------------------- | ----------------------------- |
| `Age`            | Age of the insured individual                            | Integer                       |
| `Gender`         | Gender of the insured individual                         | Categorical / Encoded Integer |
| `BMI`            | Body Mass Index of the insured individual                | Float                         |
| `No_of_Children` | Number of children/dependents                            | Integer                       |
| `Smoker`         | Smoking status of the insured individual                 | Categorical / Encoded Integer |
| `Region`         | Geographical region of the insured individual in the USA | Categorical / Encoded Integer |
| `Charges`        | Health insurance charges in USD                          | Float                         |

---

## 5. Parameter Details

### 5.1 Age

Represents the age of the insured individual.

- **Type:** Integer
- **Role:** Predictor variable
- **Example:** `25`, `42`, `60`

Age is expected to have an important relationship with insurance charges because healthcare costs and insurance risk can vary with age.

---

### 5.2 Gender

Represents the gender of the insured individual.

The categorical values are encoded numerically as follows:

| Gender | Assigned Value |
| ------ | -------------: |
| Female |              1 |
| Male   |              2 |

- **Type:** Categorical
- **Encoding:** Integer
- **Role:** Predictor variable

> **Note:** The numerical values are category labels and should not be interpreted as having a mathematical ordering.

---

### 5.3 BMI

Represents the **Body Mass Index (BMI)** of the insured individual.

- **Type:** Float
- **Role:** Predictor variable
- **Example:** `22.5`, `27.8`, `35.4`

BMI is included as a health-related feature that may have a relationship with healthcare and insurance costs.

---

### 5.4 Number of Children

Represents the number of children/dependents associated with the insured individual.

- **Parameter:** `No_of_Children`
- **Type:** Integer
- **Role:** Predictor variable
- **Example:** `0`, `1`, `2`, `3`

---

### 5.5 Smoker

Represents whether the insured individual is a smoker.

The categorical values are encoded as follows:

| Smoking Status | Assigned Value |
| -------------- | -------------: |
| Smoker         |              1 |
| Non-smoker     |              2 |

- **Type:** Categorical
- **Encoding:** Integer
- **Role:** Predictor variable

> **Note:** The numerical values represent categories rather than a continuous numerical scale.

---

### 5.6 Region

Represents the geographical region of the insured individual within the USA.

| Region    | Assigned Value |
| --------- | -------------: |
| Northwest |              1 |
| Northeast |              2 |
| Southwest |              3 |
| Southeast |              4 |

- **Type:** Categorical
- **Encoding:** Integer
- **Role:** Predictor variable

> **Note:** Region codes are categorical labels and do not indicate that one region is mathematically greater or smaller than another.

---

### 5.7 Charges

Represents the health insurance charges associated with the individual.

- **Type:** Float
- **Unit:** USD
- **Role:** **Target variable**
- **Example:** `16884.92`

The objective of the machine learning models is to estimate this value from the other available attributes.

---

## 6. Input and Output

### Input

The model receives the following individual-level attributes:

```text
Age
Gender
BMI
No_of_Children
Smoker
Region
```
