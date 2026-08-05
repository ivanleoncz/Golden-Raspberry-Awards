# Golden-Raspberry-Awards
Some truths about The Razzies.

## Requirements
Python 3.10 and Django 5.2.
> *Recommended 3.12 , [since 3.10](https://devguide.python.org/versions/#status-of-python-versions) is near EOL*
>
> *Django 5.2 has [LTS](https://www.djangoproject.com/download/).*

## Setup

### Virtual Environment
```python -m venv .venv && source .venv/bin/activate```

### Installing Packages
```pip install -r requirements.txt```

### Load Movies Dataset
```python manage.py import_worst_movies_dataset```

### Runserver
```python manage.py runserver```

## Tests
```python manage.py test app -v 2```

## API Documentation
Available via DRF Spectacular, running the server:
- [OpenAPI schema download](http://127.0.0.1:8000/api/schema/swagger-ui/)
- [Swagger UI](http://127.0.0.1:8000/api/schema/swagger-ui/)
