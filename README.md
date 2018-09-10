# Pizza order system in django 2.0 and Python 3.6

## Requirements:
- psycopg2

## Installation:
#### You should have anaconda installed prior coz conda is used to manage dependencies

### Install postgres if not installed already

### Create postgres user and give it authority so create database and login to database

```
$ sudo -i -u postgres
$ createuser --createdb --login pizza -P
  password: pizza

$ psql

# CREATE DATABASE pizza WITH OWNER pizza;
# \q

$ exit
```
### Create conda virtual environment and install dependencies

```
$ conda create -n pizza python=3.6
$ conda install django
$ conda install psycopg2
```

### Run the migrations

```
$ python manage.py makemigrations
$ python manage.py migrate
```

### Run server

```
$ python manage.py runserver
```

#### Open browser and open localhost:8000