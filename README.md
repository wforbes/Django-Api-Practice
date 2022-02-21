# Django Api Practice

This is a sandbox project to practice building an API with Django REST Framework. My goal is to step through creating the project, then experiment with different apps in combination with other front-end client projects.

## Step-by-step Notes

These notes are meant to describe the process of creating this project, step-by-step as a psuedo tutorial that can be used for future efforts.

Following along with video: [Django REST Framework Full Course For Beginners | Build REST API with Django](https://www.youtube.com/watch?v=B38aDwUpcFc)

### Installation

- Install Python 3 : ( [https://www.python.org/downloads/](https://www.python.org/downloads/) )
- Use pip to install Django and djangorestframework
  - `python -m pip install Django djangorestframework`

### Create the project

- Create a directory to act as the parent folder to your project
- Navigate to that directory in the terminal
- Run the django admin command to start the project with your desired name
  - `django-admin startproject ProjectName`
- Test that the project is working by navigating into that new project directory and running the runserver command
  - `python manage.py runserver`
- You should see output that reads 'Starting development server at <http://127.0.0.1:8000/>'
  - Navigating to that URL (or localhost:8000) in the web browser should display the 'The install worked successfully! Congratulations!' web page.

### Create the app

- From the terminal, within the project directory, run the startapp command to create the first django app with your desired name. In this project it's 'practice_api'.
  - `python manage.py startapp practice_api`
- You should be able to see a new directory in the project folder with the name that was given to the startapp command

### Create the superuser

- From the terminal, within the project directory, run the createsuperuser command
  - `python manage.py createsuperuser`
- This will give you the option to provide a specific Username and prompt you for the email and password for the superuser account.
- To test this: use the `python manage.py runserver` command to run the webserver, navigate to `localhost:8000/admin` in the web browser, and enter the username/password that was just set up. You should see the Django adminstration page once logged in.

### Add Installed Apps Configuration

- In the project folder, open the ``settings.py`` file and locate the ``INSTALLED_APPS`` array
- To register the django rest framework and our 'practice_api' app, we add two new string indexes to this array
  - 'rest_framework' and 'practice_api'
- Details: [https://www.django-rest-framework.org/#installation](https://www.django-rest-framework.org/#installation) & [https://www.django-rest-framework.org/tutorial/1-serialization/#getting-started](https://www.django-rest-framework.org/tutorial/1-serialization/#getting-started)

( End of first commit )

### Make migrations

- To create an initial database migration for the app, run the makemigrations command passing it the name of the app. In this case, that's 'practice_api'
  - `python manage.py makemigrations practice_api`

### Creating, registering, and migrating models

- In the `models.py` file of the app folder, create a class for the model, add some fields and give it a `__str__` function
  - Following along with [Django REST Framework Full Course for Beginners](https://www.youtube.com/watch?v=B38aDwUpcFc) video, I made an Article model class
- In the `admin.py` file of the app folder, import the model that was just created by referencing the model class name from the models file
  - `from .models import ModelName`
- Use the admin class that was imported by default to call the site.register function, pass in the model class name:
  - `admin.site.register(ModelName)`
  - This will allow access to the model in the admin control panel
- Once the model is created and registered, we need to migrate that change to update the database. In the terminal, run the migrate command:
  - `python manage.py migrate`

### Declaring Serializers

Using serializers this way is the more manual solution, requiring the declaration of the model fields in the serializer class and adding the create/update methods manually. This requires working with the JSONRenderer and JSONParser in order to serialize and deserialize the data between python data types and JSON strings in a manual way. It appears to be the way to do things if some business logic is required or model fields should be included selectively.

- In the app folder create a new file `serializers.py`
- Within this new file, import 'serializers' from 'rest_framework`
  - `from rest_framework import serializers`
- Import the model that was just created as well
  - `from .models import ModelName`
- Now add a serializer class for the model, named like `ModelNameSerializer`. Pass in the 'Serializer' class from 'serializers' as a parameter
  - `class ModelNameSerializer(serializers.Serializer):`
- Add the models fields to this serializer class.
  - Example: [https://www.django-rest-framework.org/api-guide/serializers/#declaring-serializers](https://www.django-rest-framework.org/api-guide/serializers/#declaring-serializers)
- Define a create and update method in the serializer class
  - Example: [https://www.django-rest-framework.org/api-guide/serializers/#saving-instances](https://www.django-rest-framework.org/api-guide/serializers/#saving-instances)

#### Testing the Model and Serializer in the Shell

- Now testing this can be done in the python shell with `python manage.py shell`
  - Here are some commands you can play with in the shell to test the model/serializer code and set up some initial data in the database
  - First, import the necessary objects:
    - `from practice_api.models import Article`
    - `from practice_api.serializers import ArticleSerializer`
    - `from rest_framework.renderers import JSONRenderer`
    - `from rest_framework.parsers import JSONParser`
  - Declare a new instance of the model
    - `m = ModelName(field1='Field One Stuff', field2='Something', field3='will@email.com')`
  - Save the instance to the database
    - `m.save()`
  - Declare a new serializer with the model instance
    - `serializer = ModelNameSerializer(m)`
  - Get the raw data from the serializer
    - `serializer.data`
  - Serialize the model instance data into JSON
    - `content = JSONRenderer().render(serializer.data)`
    - Now the `content` variable should contain a serialized json string of the model data
  - Deserialize the JSON content back into Python native datatypes
    - `import io`
    - `stream = io.BytesIO(content)`
    - `data = JSONParser().parse(stream)`
    - `serializer = ArticleSerializer(data=data)`
    - `serializer.is_valid()`
    - `serializer.validated_data`
    - `serializer.save()`
  - After creating a few objects, they can be serialized together in an ordered dictionary
    - `serializer = ModelNameSerializer(ModelName.objects.all(), many=True)`
    - `serializer.data`

( End of second commit )

### Declaring ModelSerializers

Using ModelSerializers requires less code duplication, where the model's fields can be all included automatically or declared individually. They include their own default create/update methods built in.

- In the app folder create a new file `serializers.py` or open the existing one
- Within this file, import 'ModelSerializer' from 'rest_framework.serializers'
  - `from rest_framework.serializers import ModelSerializer`
- Import the model that was just created
  - `from .models import ModelName`
- Add a serializer class for the model, named like `ModelNameSerializer`. Pass in the 'ModelSerializer' class imported
  - `class ModelNameSerializer(ModelSerializer):`
- Now all this class needs is an inner class named Meta
  - `class Meta:`
- Within this inner Meta class, add a model field with the intended model class as the value
  - `model = ModelName`
- Next add a field named 'field' with either an array of strings for the model fields to add, or a value of `__all__` to automatically include all the fields
  - `fields = ['field1', 'field2', 'field3']`
  - `fields = __all__`

#### Testing the ModelSerializer in the Shell

I created a new model named 'Post' and created a ModelSerializer for it

- Now testing this can be done in the python shell with `python manage.py shell`
  - We can use many of the same commands as the regular Serializer tests
  - Except we can also print the representation of the serializer instance
    - `serializer = PostSerializer()`
    - `print(repr(serializer))`

(End of third commit)

### Function-based API views

To reduce content here in the readme, check out the fourth commit of this repo for more exact details

- We add a function in the `practice_api/views.py` file that handles GET and POST requests called `article_list`.
  - GET returns all the articles.
  - POST parses the request data, validates it, saves it in the database and returns the data with a 201 status or returns errors with a 400 status if it was invalid
- We add a function in the same `views.py` file that handles GET, PUT, and DELETE requests for individual articles called `article_detail`
  - GET returns one article given the desired pk
  - PUT updates one article given it's pk and new data
  - DELETE removes one article given it's pk
- We create `practice_api/urls.py` file and add a url pattern for `article/` passing it the `article_list` function we just created.
- In the main project's `urls.py` file, we add a url pattern for root and include the `practice/urls.py` file in the root url pattern.

#### Testing Function-based API views

- Visiting the `localhost:8000/article` url in the web browser should display all the articles in JSON format
- Visiting the 'localhost:8000/article/1` url in the web browser should display the article with the pk id of 1 in JSON format
- Using an http testing app like Postman we can test the POST, PUT, DELETE requests.
