# Natural Language Processing (NLP) Project - Sentiment Analysis

## Overview

This repository contains code for a Natural Language Processing (NLP) project focused on sentiment analysis. The project involves exploring various machine learning algorithms for sentiment classification based on restaurant reviews.

## Dataset

The dataset used in this project is sourced from the file 'Restaurant_Reviews.tsv', containing user reviews and sentiment labels.

### Data Cleaning

The dataset underwent a cleaning process, including:

- Removal of non-alphabetic characters
- Lowercasing
- Tokenization
- Stopword removal
- Stemming

## Models Implemented

The following machine learning models were implemented and evaluated:

1. Logistic Regression
2. Naive Bayes
   - Multinomial Naive Bayes
   - Gaussian Naive Bayes
   - Bernoulli Naive Bayes
3. Decision Trees
4. Random Forest
5. Support Vector Machines (SVM)
6. k-Nearest Neighbors (k-NN)
7. XGBoost
8. LightGBM
9. CatBoost

## Evaluation Metrics

For each model, the following metrics were calculated:

- Accuracy
- Bias
- Variance

## Usage

To replicate the experiment, follow these steps:

1. Install the required dependencies:

   ```bash
   pip install pandas matplotlib scikit-learn nltk xgboost lightgbm catboost
   ```

2. Execute the Jupyter Notebook `Sentiment_Analysis.ipynb` step by step.

## Results

Here are the key results:

| Model                      | Accuracy | Bias   | Variance |
| -------------------------- | -------- | ------ | -------- |
| Logistic Regression        | 0.9333   | 0.9721 | 0.9333   |
| Naive Bayes (Bernoulli)    | 0.8775   | 0.9356 | 0.8775   |
| Naive Bayes (Gaussian)     | 0.8575   | 0.9156 | 0.8575   |
| Naive Bayes (Multinomial)  | 0.9000   | 0.955  | 0.9000   |
| Decision Tree              | 0.9300   | 0.9975 | 0.9300   |
| Random Forest              | 0.9500   | 0.9975 | 0.9500   |
| Support Vector Machine     | 0.9300   | 0.9825 | 0.9300   |
| k-Nearest Neighbour        | 0.9200   | 0.9975 | 0.9200   |
| XGBoost                    | 0.8425   | 0.9006 | 0.8425   |
| LightGBM                    | 0.7050  | 0.7687 | 0.7050   |
| Catboost                   | 0.8500   | 0.9162 | 0.8500   |

## Author

Biswajit Jena

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
