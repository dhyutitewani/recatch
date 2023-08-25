# RECATCH - Browsing Site For Movies
![image](https://github.com/virajsazzala/recatch/assets/113019331/03549c38-1fed-42cd-b459-0cd4a2aba528)


This project aims to create an interactive and user-friendly website for browsing movies, while also incorporating a robust recommendation system to enhance the user experience. This README file provides an overview of the project's structure, features, and instructions for setup.

![image](https://github.com/virajsazzala/recatch/assets/113019331/60de2ef8-287f-46ca-bf05-01c137d0eeab)


✤## Features

1. **Movie Catalog:** Browse through an extensive collection of movies with detailed information including title, genre, release year, and more.

2. **Search Functionality:** Easily find movies using a powerful search feature that enables searches by title, genre, or other relevant criteria.

3. **User Profiles:** Users can create and manage their profiles, allowing them to save favorite movies, view their watch history, and receive personalized recommendations.

4. **Recommendation System:** Our content based recommendation system employs algorithms to analyze user preferences and viewing history, suggesting movies tailored to individual tastes.

5. **User Ratings and Reviews:** Users can rate and leave reviews for movies, providing valuable feedback for others and helping to refine the recommendation system.

![image](https://github.com/virajsazzala/recatch/assets/113019331/f8b95a3c-3ae9-447d-9b14-7a5596e8d597)


✤## Technologies Used
![image](https://github.com/virajsazzala/recatch/assets/113019331/4c8ec8ea-5154-46f4-98dc-4e1a94989314)

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

![image](https://github.com/virajsazzala/recatch/assets/113019331/57a05132-db22-4544-9342-e97416d4aa6f)



✤## Getting Started

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

```
![image](https://github.com/virajsazzala/recatch/assets/113019331/6a37f7f7-23d5-4330-8518-f36cd1726751)


✤## Contribution

We welcome contributions from the community.To contribute, follow these steps:

Fork the repository.
1. Create a new branch: git checkout -b feature/new-feature.
2. Make your enhancements or fixes.
3. Commit your changes: git commit -m 'Add a new feature'.
4. Push the branch: git push origin feature/new-feature.
5. Open a pull request.

![image](https://github.com/virajsazzala/recatch/assets/113019331/ced3a88b-e616-46f9-84fa-a3f60fcefd0d)


✤## License

This project is licensed under the [MIT License](LICENSE).

---

Thank you for your interest in ReCatch!


