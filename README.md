# recipe-app-api

Recipe API Project
hello word

# Using Docker and Django

- ## Run all commands through Docker Compose
- ## docker-comose run --rm app sh -c 'python manage.py collectstatic'
- ## docker-compose, run Docker Comose command
- ## run, will start a specific container defined in config
- ## --rm, tell docker compose to remove the container once it finish running
- ## app, the name of the server or the app that to run within docker compose
- # sh -c, it's a shell command , passed ito the running container, to tell that we want to run a single command in our container
- # "python manage.py collectstatic" it's a django command for collecting static files

# How we'll handling Linting

- install flake8 package
- run it through Docker Compose
- docker-compose run --rm app sh -c "flake8"

# Testing

- Django test suite
- Setup tests per Django app
- Run tests through Docker Compose
- docker-compose run --rm app sh -c "python manage.py test"

# Create Django project

- docker-compose run --rm app sh -c "django-admin startproject app ."
