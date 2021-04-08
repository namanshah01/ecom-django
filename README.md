# Ecommerce Application - Django

## Setup

Clone the repo:
```bash
$ git clone https://github.com/namanshah01/Naman-DjangoTaskSubmission.git
```
Now cd into cloned repo, pip install the requirements
```bash
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


## Working

Click on the link to check the apps working: [click here](https://drive.google.com/file/d/1bHNTHbP9BjT4TATG-B534oE1MM6JBYF4/view?usp=sharing)

---
<h3 align="center"><b>Developed with :heart: by Naman Shah</b></h1>
