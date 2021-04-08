# Ecommerce Application - Django

## Setup (for Linux systems)

Clone the repo:
```bash
$ git clone https://github.com/namanshah01/Naman-DjangoTaskSubmission.git
```
Now create a virtualenv, cd into cloned repo and pip install the requirements
```bash
$ virtualenv Naman-DjangoTaskSubmission
$ cd Naman-DjangoTaskSubmission
$ pip3 install -r requirements.txt
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
Now set the `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD` from `settings.py` either as environment variables or hard code them into the file itself.
<br>Start the server
```bash
$ python3 manage.py runserver
```
Head over to http://localhost:8000/ so use the application

