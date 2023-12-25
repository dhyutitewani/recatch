# RECATCH
A simple movie recommendation web app powered by a movie recommendation model using cosine similarity.

Introduction
------------
Recatch Movie Recommender is a web application that provides movie recommendations based on user-selected movies. The recommendations are generated using a cosine similarity model that calculates similarity scores between movies in the dataset.

Features
--------
- Search for a movie from a predefined movie list.
- Get recommendations for similar movies.
- View movie posters and titles for the recommended movies.

Usage
-----
1. Clone the repository:

   ```git clone https://github.com/virajsazzala/recatch.git```

2. Generate the required files by running the ipynb file and put them in a ```model/``` directory

3. Install the required dependencies:

   ```pip install -r requirements.txt```

4. Run the Streamlit app:

   ```streamlit run app.py```

5. Open the web browser and go to the provided local URL (usually http://localhost:8501) to access the Recatch Movie Recommender.

How it Works
------------
1. The movie dataset is loaded into the application from a pickle file.
2. User selects a movie from the available list.
3. Upon clicking the "Recommend" button, the application uses a cosine similarity model to find similar movies to the selected one.
4. The top 5 recommended movies are displayed along with their titles and posters.

Data Source
-----------
The movie dataset used in this project comes from The Movie Database (TMDb) API. Movie posters and information are fetched from TMDb for display.

Credits
-------
- Data Source: The Movie Database (TMDb) API
- Streamlit: [https://streamlit.io/](https://streamlit.io/)
- Python Libraries: pandas, requests, pickle

Author
------
- Viraj Reddy - https://github.com/virajsazzala
- Dhyuti Amit Tewani - https://github.com/dhyutitewani


Acknowledgments
---------------
- Special thanks to the developers of Streamlit and the TMDb API for providing the tools and data used in this project.

Feel free to contribute or report issues on GitHub.
