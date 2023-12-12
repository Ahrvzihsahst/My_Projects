

# Book Recommendation System

## Table of Contents

- [Description](#description)
- [Dataset](#dataset)
- [Requirements](#requirements)
- [Usage](#usage)
- [Components](#components)
- [Files](#files)
- [Results](#results)
- [Conclusion](#conclusion)
- [References](#references)
- [License](#license)

## Description

This project implements a book recommendation system using collaborative filtering and popularity-based approaches. The system utilizes a dataset of books, user information, and ratings to provide personalized recommendations to users.

**Datasets:**
1. **Books Dataset:**
2. **Users Dataset:**
3. **Ratings Dataset:**

**Data Exploration and Cleaning:**
- Checked dimensions (shape) of each dataset.
- Investigated and handled missing values in the datasets.
- Explored and addressed duplicated entries in the datasets.

**Popularity-Based Recommender System:**
1. **Number of Ratings and Average Ratings:**
   - Calculated the number of ratings and average ratings for each book.
   - Identified popular books based on the number of ratings and average ratings.

2. **Filtering Popular Books:**
   - Filtered out books with fewer than 250 ratings.
   - Selected the top 50 popular books based on average ratings.

**Collaborative Filtering-Based Recommender System:**
1. **Filtering Users and Books:**
   - Identified users with more than 200 ratings (padhe_likhe_users).
   - Selected books with more than 50 ratings (famous_books).

2. **Creating a Ratings Matrix:**
   - Created a pivot table with users, books, and corresponding ratings.

3. **Calculating Similarity Scores:**
   - Utilized cosine similarity to compute similarity scores between books.

4. **Recommendation Function:**
   - Developed a function to recommend similar books based on a given book.

**Data Serialization:**
- Saved important data structures such as the popularity-based recommendations, collaborative filtering matrix, book details, and similarity scores using the Pickle library.

**Project Purpose:**
The purpose of the project is to provide book recommendations to users using two different approaches:
1. **Popularity-Based Recommender System:** Recommends popular books based on the number of ratings and average ratings.
2. **Collaborative Filtering-Based Recommender System:** Recommends books similar to a user's preferences by analyzing ratings and user behavior.

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

## Conclusion

The project aims to enhance the user experience by offering personalized book recommendations, catering to both popular choices and individual preferences through collaborative filtering.

## References

- [Scikit-learn Documentation](https://scikit-learn.org/stable/documentation.html)
- [Pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/index.html)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
