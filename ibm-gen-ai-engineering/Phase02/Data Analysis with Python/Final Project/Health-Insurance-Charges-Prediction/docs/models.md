## Machine Learning Models

### Simple Linear Regression

Simple Linear Regression will be used to investigate the relationship between one independent variable and insurance charges.

**General form:**

$$y = \beta_0 + \beta_1 x$$

Where:

- $y$ = predicted insurance charges
- $x$ = selected input feature
- $\beta_0$ = intercept
- $\beta_1$ = regression coefficient

**Example:**

$$\text{Insurance Charges} = \beta_0 + \beta_1(\text{Age})$$

---

### Multiple Linear Regression

Multiple Linear Regression will use several independent variables to predict insurance charges.

**General form:**

$$y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \dots + \beta_n x_n$$

**For this project:**

$$\text{Insurance Charges} = \beta_0 + \beta_1(\text{Age}) + \beta_2(\text{Gender}) + \beta_3(\text{BMI}) + \beta_4(\text{No\_of\_Children}) + \beta_5(\text{Smoker}) + \beta_6(\text{Region})$$

---

### Ridge Regression

Ridge Regression extends Linear Regression by introducing $L_2$ regularization.

It is used to reduce the impact of large model coefficients and can improve model stability when predictors exhibit multicollinearity. The model will be trained with different regularization strengths and evaluated against the standard Linear Regression model.
