

# Book Recommendation System

This project implements a book recommendation system using collaborative filtering and popularity-based approaches. The system utilizes a dataset of books, user information, and ratings to provide personalized recommendations to users.

## Table of Contents

- [Dataset](#dataset)
- [Requirements](#requirements)
- [Usage](#usage)
- [Components](#components)
- [Files](#files)
- [Results](#results)
- [References](#references)
- [License](#license)

## Dataset

The dataset consists of three main components:

1. **Books Dataset**
   - File: `books.csv`
   - Fields: ISBN, Book-Title, Book-Author, Year-Of-Publication, Publisher, Image-URL-S, Image-URL-M, Image-URL-L

2. **Users Dataset**
   - File: `users.csv`
   - Fields: User-ID, Location, Age

3. **Ratings Dataset**
   - File: `ratings.csv`
   - Fields: User-ID, ISBN, Book-Rating

## Requirements

- Python 3.x
- Pandas
- NumPy
- Scikit-learn

Install the required libraries using:

```bash
pip install pandas numpy scikit-learn
```

## Usage

1. Clone the repository:

```bash
git clone https://github.com/your-username/book-recommendation-system.git
cd book-recommendation-system
```
Make sure to replace placeholders like `your-username`.

2. Run the Jupyter notebook:

```bash
jupyter notebook
```

Open the notebook `book_recommendation_system.ipynb` and execute the cells.

## Components

The project consists of two main components:

1. **Popularity-Based Recommender System**
   - Identifies popular books based on the number of ratings and average ratings.

2. **Collaborative Filtering-Based Recommender System**
   - Uses collaborative filtering to recommend books based on user preferences and similarities.

## Files

- `book_recommendation_system.ipynb`: Jupyter notebook containing the code.
- `popular.pkl`: Pickle file containing data on popular books.
- `pt.pkl`: Pickle file containing the user-book rating matrix.
- `books.pkl`: Pickle file containing book information.
- `similarity_scores.pkl`: Pickle file containing similarity scores for collaborative filtering.

## Results

The project provides personalized book recommendations for users based on either popularity or collaborative filtering.

## References

- [Scikit-learn Documentation](https://scikit-learn.org/stable/documentation.html)
- [Pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/index.html)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
