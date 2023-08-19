# Recatch
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
