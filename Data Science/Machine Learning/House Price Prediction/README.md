# House Price Prediction using Machine Learning

In the process of buying a new house, we often encounter challenges such as fraudulent activities, negotiation complexities, and the need to research local areas. To address these issues, we present a machine learning-based model for House Price Prediction, trained on the House Price Prediction Dataset.

## Dataset Overview

The dataset contains 13 features:

1. **Id:** Record count.
2. **MSSubClass:** Type of dwelling involved in the sale.
3. **MSZoning:** General zoning classification of the sale.
4. **LotArea:** Lot size in square feet.
5. **LotConfig:** Configuration of the lot.
6. **BldgType:** Type of dwelling.
7. **OverallCond:** Overall condition rating of the house.
8. **YearBuilt:** Original construction year.
9. **YearRemodAdd:** Remodel date (same as construction date if no remodeling or additions).
10. **Exterior1st:** Exterior covering on the house.
11. **BsmtFinSF2:** Type 2 finished square feet.
12. **TotalBsmtSF:** Total square feet of basement area.
13. **SalePrice:** Target variable to be predicted.

## Libraries and Dataset Import

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_excel("HousePricePrediction.xlsx")

# Printing first 5 records of the dataset
print(dataset.head(5))
```

The dataset has dimensions (2919, 13).

## Data Preprocessing

Categorizing features by datatype and counting them:

```python
obj = (dataset.dtypes == 'object')
object_cols = list(obj[obj].index)
print("Categorical variables:", len(object_cols))

int_ = (dataset.dtypes == 'int')
num_cols = list(int_[int_].index)
print("Integer variables:", len(num_cols))

fl = (dataset.dtypes == 'float')
fl_cols = list(fl[fl].index)
print("Float variables:", len(fl_cols))
```

Categorical variables: 4, Integer variables: 6, Float variables: 3.

## Exploratory Data Analysis (EDA)

Heatmap to visualize feature correlations:

```python
plt.figure(figsize=(12, 6))
sns.heatmap(dataset.corr(), cmap='BrBG', fmt='.2f', linewidths=2, annot=True)
```

Barplot to analyze unique values of categorical features:

```python
unique_values = []
for col in object_cols:
  unique_values.append(dataset[col].unique().size)

plt.figure(figsize=(10, 6))
plt.title('No. Unique values of Categorical Features')
plt.xticks(rotation=90)
sns.barplot(x=object_cols, y=unique_values)
```

Bar graphs for individual categorical features:

```python
plt.figure(figsize=(18, 36))
plt.title('Categorical Features: Distribution')
plt.xticks(rotation=90)
index = 1

for col in object_cols:
    y = dataset[col].value_counts()
    plt.subplot(11, 4, index)
    plt.xticks(rotation=90)
    sns.barplot(x=list(y.index), y=y)
    index += 1
```

## Data Cleaning

Removing the 'Id' column:

```python
dataset.drop(['Id'], axis=1, inplace=True)
```

Handling missing values:

```python
dataset['SalePrice'] = dataset['SalePrice'].fillna(dataset['SalePrice'].mean())
new_dataset = dataset.dropna()
```

## OneHotEncoder for Label Categorical Features

```python
from sklearn.preprocessing import OneHotEncoder

s = (new_dataset.dtypes == 'object')
object_cols = list(s[s].index)
print("Categorical variables:")
print(object_cols)
print('No. of categorical features: ', len(object_cols))

OH_encoder = OneHotEncoder(sparse=False)
OH_cols = pd.DataFrame(OH_encoder.fit_transform(new_dataset[object_cols]))
OH_cols.index = new_dataset.index
OH_cols.columns = OH_encoder.get_feature_names()
df_final = new_dataset.drop(object_cols, axis=1)
df_final = pd.concat([df_final, OH_cols], axis=1)
```

## Splitting Dataset into Training and Testing

```python
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

X = df_final.drop(['SalePrice'], axis=1)
Y = df_final['SalePrice']

X_train, X_valid, Y_train, Y_valid = train_test_split(
    X, Y, train_size=0.8, test_size=0.2, random_state=0)
```

## Model and Accuracy

### Support Vector Machine (SVM)

```python
from sklearn import svm
from sklearn.svm import SVC
from sklearn.metrics import mean_absolute_percentage_error

model_SVR = svm.SVR()
model_SVR.fit(X_train, Y_train)
Y_pred_SVR = model_SVR.predict(X_valid)

print(mean_absolute_percentage_error(Y_valid, Y_pred_SVR))
```

### Random Forest Regression

```python
from sklearn.ensemble import RandomForestRegressor

model_RFR = RandomForestRegressor(n_estimators=10)
model_RFR.fit(X_train, Y_train)
Y_pred_RFR = model_RFR.predict(X_valid)

mean_absolute_percentage_error(Y_valid, Y_pred_RFR)
```

### Linear Regression

```python
from sklearn.linear_model import LinearRegression

model_LR = LinearRegression()
model_LR.fit(X_train, Y_train)
Y_pred_LR = model_LR.predict(X_valid)

print(mean_absolute_percentage_error(Y_valid, Y_pred_LR))
```

### CatBoost Classifier

```python
from catboost import CatBoostRegressor

cb_model = CatBoostRegressor()
cb_model.fit(X_train, Y_train)
preds = cb_model.predict(X_valid)

cb_r2_score = r2_score(Y_valid, preds)
cb_r2_score
```

## Conclusion

In conclusion, the SVM model shows the best accuracy with a mean absolute percentage error of approximately 0.18. Further improvements could involve using ensemble learning techniques like Bagging and Boosting for enhanced results.
