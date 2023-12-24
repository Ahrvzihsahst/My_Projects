# Data Cleaning and Analysis for Loan Repayment Prediction


## Table of Contents

- [Introduction](#introduction)
- [Dependencies](#dependencies)
- [Getting Started](#getting-started)
- [EDA](#eda)
- [Results](#results)
- [Contribution](#contributing)
- [License](#license)

## Introduction

This notebook contains exploratory data analysis (EDA) on bank loan default risk. It is written in Python and uses data from the Loan Defaulter dataset, which contains information about 1000 loan applicants who defaulted or did not default on their loans. The notebook is an example of how EDA can be used to explore and understand data before applying machine learning techniques. It demonstrates how EDA can help to identify patterns, trends, outliers, relationships, anomalies, and insights from the data that can inform decision making and problem solving.

## Dependencies

- Python (3.11)
- Libraries: NumPy, Pandas, Matplotlib, Seaborn, Missingno
- Jupyter Notebook

## Getting Started

Provide instructions on how to set up the project locally. Include steps for installing dependencies and running the code.

```bash
# Clone the repository
git clone https://github.com/your-username/your-repo.git

# Change to the project directory
cd your-repo

# Install dependencies
pip install -r requirements.txt

# Run the project
python your_script.py
```

## EDA

1. **Importing Libraries:** You've imported necessary libraries like NumPy, Pandas, Matplotlib, Seaborn, and Missingno.

2. **Data Inspection and Cleaning:**
   - Loaded a dataset (`application_data.csv`) using Pandas.
   - Checked the structure and information about the dataset.
   - Handled missing values by visualizing them and dropping unnecessary columns.
   - Inspected and dropped columns based on the percentage of missing values.
   - Explored and visualized data distribution, correlations, and outliers.
   - Converted and standardized some numerical features.
   - Binned numerical columns to create categorical columns.
   - Converted negative days to positive days in date-related columns.
   - Converted numerical columns to categorical based on certain criteria.
   - Imputed missing values in categorical columns.

3. **Data Analysis and Visualization:**
   - Analyzed and visualized the imbalance in the target variable.
   - Plotted univariate and bivariate categorical analyses using bar plots and point plots.
   - Analyzed the relationship between income type and income amount range.
   - Explored and visualized correlations between numerical variables.
   - Examined the distribution of numerical columns related to the amount using density plots.

4. **Functions:**
   - Created functions for univariate categorical analysis (`univariate_categorical`).
   - Defined a function for bivariate bar plots (`bivariate_bar`).
   - Implemented a function for bivariate relational plots (`bivariate_rel`).
   - Developed functions for univariate categorical analysis on the merged dataframe (`univariate_merged`).
   - Created a function for merged point plots (`merged_pointplot`).

5. **Categorical Variable Analysis:**
   - Explored various categorical variables such as contract type, gender, car ownership, realty ownership, etc., based on loan repayment status.

6. **Numeric Variables Analysis:**
   - Analyzed and visualized correlations between numeric variables.
   - Explored the distribution of numerical columns related to amounts using density plots.


## Results
 These are the factors  which can be taken into considerations to decide that an applicant will repay:
- NAME_EDUCATION_TYPE: Academic degree has less defaults.
- NAME_INCOME_TYPE: Student and Businessmen have no defaults.
- REGION_RATING_CLIENT: RATING 1 is safer.
- ORGANIZATION_TYPE: Clients with Trade Type 4 and 5 and Industry type 8 have defaulted less than 3%
- DAYS_BIRTH: People above age of 50 have low probability of defaulting
- DAYS_EMPLOYED: Clients with 40+ year experience having less than 1% default rate
- AMT_INCOME_TOTAL:Applicant with Income more than 700,000 are less likely to default
- NAME_CASH_LOAN_PURPOSE: Loans bought for Hobby, Buying garage are being repayed mostly.
- CNT_CHILDREN: People with zero to two children tend to repay the loans.

  
Decisive Factor whether an applicant will be Defaulter:
- CODE_GENDER: Men are at relatively higher default rate
- NAME_FAMILY_STATUS : People who have civil marriage or who are single default a lot.
- NAME_EDUCATION_TYPE: People with Lower Secondary & Secondary education
- NAME_INCOME_TYPE: Clients who are either at Maternity leave OR Unemployed default a lot.
- REGION_RATING_CLIENT: People who live in Rating 3 has highest defaults.
- OCCUPATION_TYPE: Avoid Low-skill Laborers, Drivers and Waiters/barmen staff, Security staff, Laborers and Cooking staff as the default rate is huge.
- DAYS_BIRTH: Avoid young people who are in age group of 20-40 as they have higher probability of defaulting
- DAYS_EMPLOYED: People who have less than 5 years of employment have high default rate.
- CNT_CHILDREN & CNT_FAM_MEMBERS: Client who have children equal to or more than 9 default 100% and hence their applications are to be rejected.
- AMT_GOODS_PRICE: When the credit amount goes beyond 3M, there is an increase in defaulters.

## Contributing

Feel free to contribute to this project by forking the repository and submitting pull requests. Bug reports, suggestions, and feature requests are also welcome.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

