# Data Cleaning and Analysis for Loan Repayment Prediction


## Table of Contents

- [Introduction](#introduction)
- [Dependencies](#dependencies)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [EDA](#analysis)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

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

## Usage

Explain how to use your project, including any configuration files, command-line arguments, or input data.

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

Share the main results or outcomes of your project. Include visualizations or other relevant materials.

## Contributing

Provide information on how others can contribute to your project. Include guidelines for submitting issues, feature requests, and pull requests.

## License

Specify the license under which your project is released.

## Acknowledgments

Give credit to any resources, tools, or individuals that influenced or supported your project.

```

Feel free to customize the template to better suit your project.
