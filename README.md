# Activity Generator

[![codecov](https://codecov.io/gh/amakarudze/activity_generator/branch/main/graph/badge.svg?token=MoWiBNRAER)](https://codecov.io/gh/amakarudze/activity_generator)

This API is a fun project developed using Django and Django Rest Framework. The API suggests fun things one can do when they are bored.

## Installation
### Requirements
This API requires has been developed and tested on: 
* Python 3.9+
* Django 4.0.1
* Django Rest Framework >=3.13.1
* Postgres 12.1

### Installing
* Clone this repo.
* Create a virtual environment and activate it.
* Run `pip install -r requirements.txt` to install the requirements in your virtual environment.
* Create an `.env` file in the root folder of your project, following the `.env_example` to provide environment variables for your API.
* Run `python manage.py migrate` to run migrations.
* Run `python manage.py runserver` to run the API.

### Testing
To test using automated tests, run:

`coverage run -m pytest`

To test manually, open the URL you get from running 

`python manage.py runserver` 

and create a user, get a token and then add it to your browser's [ModHeader](https://modheader.com/) extension or use [Postman](https://www.postman.com/).


## Usage
### Creating an account
To use this API, you need to create a user account for yourself by either using the `python manage.py createsuperuser` command or visiting `http://127.0.0.1:8000/accounts/create/` url or making a `POST` request to the URL `http://127.0.0.1:/accounts/create/`in [`Postman`](https://www.postman.com/), assuming your server is running on port `8000` which is the usual Django server port.

The values required in the payload are:
* email
* first_name
* last_name
* password

A sample payload would be:

```
JSON
payload = {
  "email": "test@test.com",
  "first_name": "Test",
  "last_name": "Test",
  "password": "somepassword"
}
```

### Authentication
This API uses Django Rest Framework's Token Authentication. To create a token, make a `POST` request to `http://127.0.0.1:8000/accounts/token/` with the `email` and `password` as the payload or just enter them in the form in the given URL to get a token. You can use this token to authenticate in the browser using [ModHeader](https://modheader.com/) or include the token in your request in [Postman](https://www.postman.com/).

### Adding Tags and Activities
To add an activity, you first need to create tags. You can do so my making a `POST` request to `http://127.0.0.8000/tags/` with a payload that only requires a `name` value.

To add an activity, make a `POST` request to`http://127.0.0.1:8000/activities/` with a payload that has `name`, `nature` and `tag`. The value of the tag should be a primary key (integer).

Alternatively, you can log in with your superuser account in the API's admin section using the URL `http://127.0.0.1:8000/admin/` and add tags and activities from there.

### Getting activities to do when bored
To get suggestions of activities you can do when you're bored, you can send a `GET` request to `http://127.0.0.1/activities/` and get a list of all activities you have saved. To get activities with a particular `name` or `nature`, make `GET` requests with the following parameters respectively:
* `http://127.0.0.1/activities/?name=hiking`
* `http://127.0.0.1/activities/?nature=?relaxing` 
just as examples of query parameters.

Enjoy!