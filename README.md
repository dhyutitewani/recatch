# Recatch
## Setup and Installation
```bash
# Clone this repository
git clone https://github.com/virajsazzala/recatch.git

# Create a virtual enviorment
pipenv shell

# Install requirements to that virtual enviorment
pipenv install

# Setting up django-tailwind
python manage.py tailwind install

# Run dev server
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
python manage.py tailwind start
