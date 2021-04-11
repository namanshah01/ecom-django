# Ecommerce Application - Django

Ecommerce website made using django

## Functionality

- Custom user
- Login / Register / Update Password via mail
- Product add / update / delete permission only to superuser
- Add / Remove from cart functionality through AJAX
- Checkout option (razor pay yet to be integrated)

## Setup (for Unix / Linux systems)

Clone the repo:
```bash
$ git clone https://github.com/namanshah01/ecom-django.git
```
Now cd into cloned repo, create a virtualenv and pip install the requirements
```bash
$ cd ecom-django
$ virtualenv env
$ pip3 install -r requirements.txt
$ source env/bin/activate
```
Create and apply the migrations
```bash
$ python3 manage.py makemigrations
$ python3 manage.py migrate
```
Create a superuser for admin privilages
```bash
$ python3 manage.py createsuperuser
```
Now set the `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD` and `SECRET_KEY` from `settings.py` either as environment variables or hard code them into the file itself.
<br>Start the server
```bash
$ python3 manage.py runserver
```
Head over to [localhost:8000](http://localhost:8000/), to use the application

---
<h3 align="center"><b>Developed with :heart: by Naman Shah</b></h3>
