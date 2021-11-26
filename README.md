A project built with Django web framework and Bootstrap

To get started with the project:

1- Clone the repository: git clone 'https://github.com/MoustafaShaaban/Simple_Django_Blog.git'

2- Create a virtual environment like pipenv and activate it.

3- Install requirements.txt: pipenv install -r requirements.txt

4- Create the database and super user by running the following commands:
`python manage.py migrate`
`python manage.py makemigrations blog`
`python manage.py migrate blog`
`python manage.py createsuperuser`

5- Create a superuser: python manage.py createsuperuser

6- Run the project: python manage.py runserver
