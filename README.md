# Pagination and Filtering Django Project

In this project the user data are shows pagination order. The data can be filter low to high, high to low. User can search location based data and price based data also. In this project we store the database in https://railway.app/ 

## Technology and Tools
- FrontEnd: HTML, CSS, JS, Bootstrap 
- Programming Language: Python
- Framework: Django
- Database: PostgreSQL (https://railway.app/ )

## Author

- [Shohag Rana](https://github.com/Shohag-Rana)

## Prerequisites
  - Python 3.9+
  - Postgres
  - Virtualenv and Pip
  - A CPU with at least 2 core
  - IDE (VS, Pycharm)

## Installation and Project Setup

- install virtual environment-wrapper:- "pip/pip3 install virtualenvwrapper-win"
- create virtual environment:- "virtualenv env"
- activate virtual env :- ".\env\Scripts\activate"
- cd python_django_assignment
- pip/pip3 install -r requirements.txt
- python/python3 manage.py makemigrations
- python/python3 manage.py migrate
- python/python3 manage.py createsuperuser
- python/python3 manage.py runserver

## Feature of this Project

- The data are render from online server railway.app.
- The property and category data are shows pagination order.
- User can filter data low to high or high to low order.
- User can search location and show specific location data.
- Admin are maintain all the project structure.

## Project File Structure and Description
- env :- virtual environment
- static :- This folder contains all the static files (css, js, images).
- myapp :- This is application folder contain all the application file [views, models, admin, urls]
- python_django_assignment:- This is the root project folder
- templates :- Contain all the jinja2 template files

## Conculation

In this django project i use jinja2 template to render postgresql backend data into frontend. postgreSQL data are stored into online server https://railway.app/. The filter and location search option are included in this
project. All the data are shows in pagination order. Thank you all the people
 
