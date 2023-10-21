# Movie Recommendation System

This is a simple movie recommendation system created using Python and pandas.

## Dataset

We use two datasets: `tmdb_5000_movies.csv` and `tmdb_5000_credits.csv`. These datasets contain information about movies, including details such as budget, genres, keywords, cast, crew, and more.

## Data Preprocessing

We start by loading the datasets and merging them on the movie title. After cleaning the data, we extract relevant information from columns such as `genres`, `keywords`, `cast`, and `crew`. We also create a new column, `tags`, by combining several text columns.

## Text Preprocessing

Text data in the `tags` column is preprocessed using the following steps:

- Convert to lowercase.
- Tokenization and stemming using NLTK's Porter Stemmer.
- Count Vectorization with a maximum of 5000 features and English stop words.

## Movie Recommendation

We calculate the cosine similarity between movies based on their tags. Then, we recommend movies similar to a given movie title.

## Usage

```python
recommend('Avatar')
This will recommend movies similar to 'Avatar'.

## Results
Here are some movie recommendations for 'Avatar':

Aliens vs Predator: Requiem
Aliens
Falcon Rising
Independence Day
Titan A.E.

Feel free to modify and use this code for your own movie recommendation system.
