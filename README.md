# RECATCH - Browsing Site For Movies
![image](https://github.com/virajsazzala/recatch/assets/113019331/03549c38-1fed-42cd-b459-0cd4a2aba528)


This project aims to create an interactive and user-friendly website for browsing movies, while also incorporating a robust recommendation system to enhance the user experience. This README file provides an overview of the project's structure, features, and instructions for setup.

## Features

1. **Movie Catalog:** Browse through an extensive collection of movies with detailed information including title, genre, release year, and more.

2. **Search Functionality:** Easily find movies using a powerful search feature that enables searches by title, genre, or other relevant criteria.

3. **User Profiles:** Users can create and manage their profiles, allowing them to save favorite movies, view their watch history, and receive personalized recommendations.

4. **Recommendation System:** Our content based recommendation system employs algorithms to analyze user preferences and viewing history, suggesting movies tailored to individual tastes.

5. **User Ratings and Reviews:** Users can rate and leave reviews for movies, providing valuable feedback for others and helping to refine the recommendation system.

## Technologies Used
#### Backend
Django for database management.
#### Frontend
1. Utilized Django's templating engine along with HTML and CSS for responsive user interfaces.
2. Anime.js for animations and interactive UI elements.
#### Frontend Build
1. Webpack for asset bundling, and enabling modern JavaScript features.
2. PostCSS for advanced CSS transformations.
3. PurgeCSS to remove unused CSS.
3. ESLint for maintaining code quality.
#### Machine Learning:
1. Python along with libraries like scikit-learn, TensorFlow, NumPy, and Pandas for developing the recommendation system.
2. scikit-learn for data preprocessing, model training, and evaluation.
3. TensorFlow for building and training deep learning models for personalized movie recommendations.


## Getting Started

## Setup and Installation
```bash
# Clone this repository
git clone https://github.com/virajsazzala/recatch.git

cd recatch

# Create a virtual enviorment
pipenv shell

# Install requirements to that virtual enviorment
pipenv install


# Setting up django-tailwind
python manage.py tailwind install

# Migrations
python manage.py makemigrations
python manage.py migrate

# To run dev server run these commands in different terminals
python manage.py runserver
python manage.py tailwind start

## Contribution

We welcome contributions from the community.To contribute, follow these steps:

Fork the repository.
1. Create a new branch: git checkout -b feature/new-feature.
2. Make your enhancements or fixes.
3. Commit your changes: git commit -m 'Add a new feature'.
4. Push the branch: git push origin feature/new-feature.
5. Open a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

---

Thank you for your interest in ReCatch!


