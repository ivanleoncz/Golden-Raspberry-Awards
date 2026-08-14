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

### Runserver

In-memory database. No persistence. Each process start or code modification, sets the database to its initial state:

```python manage.py runserver```

If you want to preserve the database state during the life of the process:

```python manage.py runserver --noreload```


#### Debugging
In-file database. Persistence guaranteed across restarts. Code changes will not trigger process reloading:

```MOVIES_DEBUG=1 python manage.py runserver```

## Tests
```python manage.py test app -v 2```

## Django Admin
Credentials are provided in the console when running the server. [Authenticate](http://127.0.0.1:8000/admin/) with user `grp-admin`.

> **Notice:** *If the application is running in DEBUGGING mode (in-file database), credentials might have already being set. E.g: **grp-admin / grp-admin***

## API Documentation
Available via DRF Spectacular, running the server:
- [Swagger UI](http://127.0.0.1:8000/api/schema/swagger-ui/), for reviewing endpoint and testing them in browser.
- [OpenAPI YAML schema](http://127.0.0.1:8000/api/schema/swagger-ui/), for Postman-like services.
