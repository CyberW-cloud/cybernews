# Cybernews API
## Python test assessment
### for DevelopsToday 
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

##### API suggets simple list of news:
Articles with ability of upvoting and commenting.
CRUD API provided for article/comment management.
API enpoints provided for upvote management.

#### [Postman collection](https://documenter.getpostman.com/view/13254397/TVeiEBA8)
#### I didn't get how to [Heroku]()
### Stable on:

  - Python v3.8
  - Docker v19

# Instalation:
Clone github repository
```sh
git clone https://github.com/CyberW-cloud/cybernews
```

Create dev.env file with following content:
```sh
SQL_ENGINE=django.db.backends.postgresql_psycopg2
SQL_DATABASE = %DBname%
SQL_USER = %postgres%
SQL_PASSWORD = %123456%
SQL_HOST = db
SQL_PORT = 5432
```
##### %values% - values to be changed 
%DBname% - name of database
%postgres% - postgres user login
%123456% - postgres user password

Run up your docker:
```sh
docker-compose build
docker-compose up -d
```
To create superuser use this command in your cybernews-web docker container:
```sh
python3 manage.py createsuperuser
```
To add recurring job for upvote daily reset just run in your cybernews-web docker container:
```sh
python3 manage.py runjobs daily
```
Server admin panel will be avaliable by the address:
```sh
http://127.0.0.1:8000/admin/
```

Now you are free to use this API!
