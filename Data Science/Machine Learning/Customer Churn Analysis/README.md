# Customer Churn Analysis - Machine Learning Project

## Overview

This repository contains the code for a machine learning project focused on predicting customer churn. Customer churn refers to the phenomenon of customers discontinuing their relationship with a business. The project employs various classification algorithms to analyze a dataset and make predictions regarding customer behavior.

## Table of Contents

- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Rank TAble](#rank-table)
- [Who Can Use It](#who-can-use-it)
- [Impact](#impact)
- [Contributing](#contributing)
- [License](#license)

## Introduction

In this project, we aim to understand and predict customer churn using machine learning techniques. The project involves the following key steps:

1. **Data Loading and Exploration:** We start by importing necessary libraries, loading the dataset, and exploring its structure and content.

2. **Data Preprocessing:** The data is preprocessed to handle categorical variables, missing data, and to split the dataset into training and testing sets.

3. **Applying Classification Algorithms:** Various classification algorithms, including Logistic Regression, Naive Bayes, Decision Trees, Random Forest, Support Vector Machines, k-Nearest Neighbors, and Gradient Boosting (XGBoost, LightGBM, CatBoost) are applied to train models and make predictions.

4. **Model Evaluation:** We evaluate the performance of each model using metrics such as accuracy, bias, variance, and classification reports.

5. **Comparison of Models:** Finally, we compare the accuracy of different models to determine which one is most effective in predicting customer churn.

## Project Structure

The project structure is organized as follows:

- **`src/`**: Contains the source code for the machine learning project.
- **`data/`**: Placeholder for the dataset used in the project.
- **`README.md`**: Provides an overview of the project, usage instructions, and other relevant information.

## Installation

To run this project locally, follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/customer-churn-analysis.git`
2. Navigate to the project directory: `cd customer-churn-analysis`
3. Install the required dependencies: `pip install -r requirements.txt`
Install these libraries using:

## Usage

To use this project, follow these steps:

1. Ensure you have installed the required dependencies.
2. Run the Jupyter Notebook or Python script containing the code (`Customer Churn Analysis.ipynb`).
3. Explore the results and analyses provided in the notebook or script.

## Dependencies

The project relies on the following Python libraries:

- NumPy
- Pandas
- Matplotlib
- scikit-learn
- XGBoost
- LightGBM
- CatBoost
  
```bash
pip install numpy pandas matplotlib scikit-learn xgboost lightgbm catboost
```

## Rank Table

### Without GridSearchCv
|index|Algorithm|Accuracy|Bias|Variance|
|---|---|---|---|---|
|0|LogisticRegression|78\.9|78\.9|78\.9|
|1|DecisionTreeClassifier|80\.2|100\.0|80\.2|
|2|RandomForestClassifier|86\.5|99\.9|86\.5|
|3|SVC|79\.7|79\.6|79\.7|
|4|KNeighborsClassifier|76\.4|81\.6|76\.4|
|5|GaussianNB|78\.4|78\.5|78\.4|
|6|MLPClassifier|78\.3|78\.9|78\.3|
|7|VotingClassifier|81\.2|85\.0|81\.2|

### With Grid Searchcv
|index|Algorithm|Accuracy|
|---|---|---|
|0|Logistic Regression|78\.9|
|1|Bernoulli Naive Bayes|78\.60|
|2|Gaussian Naive Bayes|78\.45|
|3|MultiNomial Naive Bayes|54\.40|
|4|Decision Trees|85\.15|
|5|Random Forest|86\.55|
|6|Support Vector Machines \(SVM\)|79\.75|
|7|k-Nearest Neighbors \(k-NN\)|77\.9|
|8|XGBoost|85\.25|
|9|LightGBM|86\.9|

### Who Can Use It

This code is intended for use by data scientists, machine learning engineers, or analysts responsible for customer analytics and retention strategies within a business or organization.

### Impact

The impact of this code lies in its potential to help businesses reduce customer churn. 
By predicting which customers are more likely to leave, companies can take proactive measures to retain them, leading to increased customer satisfaction and business profitability. 
Additionally, the code provides a framework for comparing and selecting the most suitable machine learning model for a given dataset.

## Contributing

Feel free to contribute to this project by forking the repository and submitting pull requests. Bug reports, suggestions, and feature requests are also welcome.
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
