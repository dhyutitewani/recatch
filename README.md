Certainly! Your `app.py` code appears to be a simple Movie Recommender System using Streamlit and cosine similarity. I'll provide some documentation for your code:

### Movie Recommender System Documentation

**1. Introduction:**
   - This is a Movie Recommender System built using Python and Streamlit, which helps users discover movies based on their preferences.

**2. Dependencies:**
   - The following Python libraries and modules are required:
     - `pickle`: For reading pickled data containing movie information and similarity scores.
     - `streamlit`: To create the web-based user interface.
     - `requests`: For making HTTP requests to fetch movie data from a third-party API.
     - `pandas`: For data manipulation and displaying movie recommendations.
     - `sklearn.feature_extraction.text.CountVectorizer`: For text vectorization.

**3. Data Sources:**
   - The movie data is stored as pickled files (`movie_list.pkl` and `similarity.pkl`), which are loaded into the system.
   - Movie poster images and additional information are fetched from "The Movie Database" (TMDb) API.

**4. Functions:**

   - `fetch_poster(movie_id)`: This function takes a `movie_id` as input, fetches the movie's poster image URL from TMDb, and returns the full image URL.

   - `recommend(movie)`: Given a selected `movie`, this function finds similar movies based on cosine similarity.
     - It calculates cosine similarity scores for all movies in the dataset.
     - Sorts movies based on their similarity scores in descending order.
     - Returns the names and poster URLs of the top 5 recommended movies.

**5. Streamlit UI:**
   - The Streamlit web application consists of the following components:
     - A header displaying "Movie Recommender System."
     - A dropdown select box to choose a movie from the available options.
     - A button labeled "Show Recommendation" to trigger the recommendation process.
     - Five columns to display the recommended movies' names and poster images.

**6. Movie Selection and Recommendation:**
   - Users select a movie from the dropdown menu.
   - When the "Show Recommendation" button is clicked, the system retrieves and displays the top 5 movie recommendations along with their poster images.

**7. Recommendation Display:**
   - The recommendations are displayed in five columns, each containing the movie's name and poster image.

**8. Recommendation Algorithm:**
   - The system uses cosine similarity to find similar movies. It creates a matrix of movie descriptions and calculates the cosine similarity scores between them.

**9. Poster Retrieval:**
   - The poster images of recommended movies are fetched from TMDb using their movie IDs.

**10. How to Run:**
    - Make sure you have the required libraries installed (e.g., `streamlit`, `requests`, `pandas`).
    - Run the Streamlit app with the command `streamlit run app.py` in your terminal.

**11. Acknowledgments:**
    - The movie data and similarity scores are precomputed and loaded from pickled files.
    - The poster images and additional movie details are retrieved from TMDb.

**12. Future Improvements:**
    - You can further enhance this recommender system by incorporating user feedback and ratings to provide personalized recommendations.

This documentation should help users understand how your Movie Recommender System works and how to interact with it using the Streamlit interface.