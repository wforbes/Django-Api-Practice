# Django Api Practice

This is a sandbox project to practice building an API with Django REST Framework. My goal is to step through creating the project, then experiment with different apps in combination with other front-end client projects.

## Step-by-step Notes

These notes are meant to describe the process of creating this project, step-by-step as a psuedo tutorial that can be used for future efforts.

### Installation

- Install Python 3 : ( [https://www.python.org/downloads/](https://www.python.org/downloads/) )
- Use pip to install Django and djangorestframework
  - ```python -m pip install Django djangorestframework```

### Create the project

- Create a directory to act as the parent folder to your project
- Navigate to that directory in the terminal
- Run the django admin command to start the project with your desired name
  - ```django-admin startproject ProjectName```
- Test that the project is working by navigating into that new project directory and running the runserver command
  - ```python manage.py runserver```
- You should see output that reads 'Starting development server at <http://127.0.0.1:8000/>'
  - Navigating to that URL (or localhost:8000) in the web browser should display the 'The install worked successfully! Congratulations!' web page.

### Create the app

- From the terminal, within the project directory, run the startapp command to create the first django app with your desired name.
  - ```python manage.py startapp app_name```
- You should be able to see a new directory in the project folder with the name that was given to the startapp command

### Create the superuser

- From the terminal, within the project directory, run the createsuperuser command
  - ```python manage.py createsuperuser```
- This will give you the option to provide a specific Username and prompt you for the email and password for the superuser account.
- To test this: use the ```python manage.py runserver``` command to run the webserver, navigate to ```localhost:8000/admin``` in the web browser, and enter the username/password that was just set up. You should see the Django adminstration page once logged in.

(End of first commit)