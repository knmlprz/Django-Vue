## Backend

Install dependencies

```sh
poetry install
```

Run migrations:

```sh
poetry run python manage.py migrate
```

Create superuser:

```sh
poetry run python manage.py createsuperuser
```

Start dev server:

```sh
poetry run python manage.py runserver
```

go to http://localhost:8000/api/docs to see the OpenAPI documentation

## Authentication

TBA
