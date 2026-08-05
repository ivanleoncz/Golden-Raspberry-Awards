# Golden-Raspberry-Awards
Some truths about The Razzies.

## Requirements
Python 3.10 and Django 5.2.
> *Recommended 3.12 , [since 3.10](https://devguide.python.org/versions/#status-of-python-versions) is near EOL*
>
> *Django 5.2 has [LTS](https://www.djangoproject.com/download/).*

## Setup & Run

### Virtual Environment
```python -m venv .venv && source .venv/bin/activate```

### Installing Packages
```pip install -r requirements.txt```

### Migrations
```python manage.py migrate```

### Load Movies Dataset
```python manage.py import_worst_movies_dataset```

### Runserver
```python manage.py runserver```

## Tests
```python manage.py test app -v 2```

## Django Admin
[Authenticate](http://127.0.0.1:8000/admin/) with `grp-admin` string for both Username and Password.

## API Documentation
Available via DRF Spectacular, running the server:
- [Swagger UI](http://127.0.0.1:8000/api/schema/swagger-ui/), for reviewing endpoint and testing them in browser.
- [OpenAPI YAML schema](http://127.0.0.1:8000/api/schema/swagger-ui/), for Postman-like services.
