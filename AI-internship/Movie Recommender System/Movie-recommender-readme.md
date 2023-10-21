# Movie Recommendation System

This README provides an overview of a movie recommendation system built using Python and the scikit-learn library. The system uses natural language processing techniques to recommend movies based on their similarity to a given movie.

## Dataset

The system uses two datasets:
- `tmdb_5000_movies.csv`: This dataset contains information about movies, including details like budget, genres, keywords, original language, and more.
- `tmdb_5000_credits.csv`: This dataset contains information about the cast and crew of the movies.

## Code Structure

The code is structured as follows:

1. **Data Loading**: The code starts by importing necessary libraries, such as NumPy and Pandas. It loads the two datasets into Pandas DataFrames (`movies` and `credits`) from CSV files.

2. **Data Preprocessing**: The code then performs various data preprocessing steps, including:
   - Merging the `movies` and `credits` DataFrames based on the movie title.
   - Cleaning and transforming the data, such as converting lists of genres, keywords, cast, and crew into more usable formats.

3. **Text Preprocessing**: Further data preprocessing includes:
   - Lowercasing all text data.
   - Stemming text data using the Porter Stemmer.
   - Creating a new DataFrame (`new_df`) that contains the movie title and processed tags.

4. **Feature Extraction**: Using Count Vectorization, the code extracts features from the processed tags.

5. **Recommendation**: The system uses cosine similarity to calculate the similarity between movies based on their tag vectors. It can recommend movies similar to a given movie by finding the most similar movies in the dataset.

6. **Movie Recommendation Function**: The code defines a function, `recommend(movie)`, which takes a movie title as input and recommends five similar movies based on the processed tags and cosine similarity.

## Usage

To use this movie recommendation system, you can follow these steps:

1. Ensure you have the required libraries installed, such as NumPy, Pandas, scikit-learn, and NLTK.

2. Load the provided datasets (`tmdb_5000_movies.csv` and `tmdb_5000_credits.csv`) or replace them with your own dataset.

3. Execute the code, which preprocesses the data and builds the recommendation system.

4. Call the `recommend(movie)` function, providing the title of a movie for which you want recommendations. The function will return a list of recommended movies.

## Example

As an example, the code was tested with the movie 'Avatar', and it recommended the following movies as similar:
- Terminator 2: Judgment Day
- Aliens
- The Abyss
- Battle Beyond the Stars
- Star Wars: Clone Wars
