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
- docker-compose up

# GitHub Actions

- Automation tool
- Similar to Travis-CI, Gitlab CI/CD, Jenkins
- Run jobs when code changes
- Automate tasks

## Common uses of gitHub Actions

- Deployment
- Code linting
- Unit tests

## gitHub Actions pricing

- Charged per minutes
- 2000 free minutes
- Various plans available, to by more minutes

# Docker Hub

- Needed to pull base images
- Rates limits
  - Anonymous: 100/6h
  - Authenticated: 200/6h
- GitHub Actions uses shared IP addresses
  - Limit applied to all users
- Authenticated with Docker Hub
  - 200 pulls per 6h all to ourselves!
  - More than enough for most projects
- Additional plans available

# Django test framework

- ## Django test framework its build on the top of unit test library
- ## Django adds features
- ### Test client - dummy web browser
- ### Simulate authentication
- ### Temporary database
- ## Django REST Framework adds features
- ### API test client

- ## where do you put tests ?
- ### Placeholder test.py added to each app
- ### Or create tests/ subdirectory to split tests up
- ### keep in mind:
- #### Only use tests.py or tests/ directory (not both)
- #### Test modules must start with test
- #### Test directory must contain _init_.py

- ## Test Database
- ### Test code that uses the DB
- ### Specific database for test, happens for every test (by default)

- ## Test classes (or types)
- ### SimpleTestCase
- #### No database integration
- #### Useful if no database is required for your test
- #### This , can save you executing tests

- ### TestCase (mostly used)
- #### Database integration
- #### Useful for testing code that uses the database

- ### Writing tests
- #### Import test class
- ##### SimpleTestCase - Non Database
- ##### TestCase - Database
- #### Import Object to test
- #### Define test class
- #### Add test method
- #### Setup inputs
- #### Execute code to be tested
- #### Check output

# TDD

# Mocking

- ## Whats Mocking ?

  - ### Override or change behavior of dependencies
  - ### Avoid unintended side effects
  - ### Isolate code being tested

- ## Why use mocking ?

  - ### Avoid relying on external services

    - #### Can't guarantee they will be available
    - #### Makes tests unpredictable and inconsistent

  - ### Avoid unintended consequences

    - #### Accidentally sending emails
    - #### Overloading external services

  - ### Another benefit
    - #### Speed up tests

- ## How to mock code ?
  - ### Use unittest.mock (comes with build in python) with tools :
    - #### MagicMock / Mock -> ### Replace real objects
    - #### patch -> ### Overrides code for tests

# Testing Web Request with Django and Django REST Framework

## Testing APIs

- ### Make actual requests
- ### Check result

## Django REST Framework give APIClient

- ### Based on top of the Django's TestClient
- ### Make requests
- ### Check result
- ### Override authentication

## Using the APIClient:

- ### Import APIClient
- ### Create client
- ### Make request
- ### Check result

# Common testing problems with Django and Django REST Framework

- ## Test not running
- ## Run less tests than you defined
- ## Possible reasons for tests not running:
  - ### Missing **init**.py in tests/dir
  - ### Or, Indentation of test cases
  - ### Or, Missing test prefix for method
- ## ImportError when running tests
- ## Possible reason for ImportError
  - ### Both tests/ directory and tests.py in your app

# Database

- ## PostgreSQL

  - ### Popular open source DB
  - ## Integrate well with Django

- ## Docker Compose

  - ### Defined with project(re-usable)
  - ### Persistent data using volumes
  - ### Handles network configuration
  - ### Environment variable configuration

- ## Architecture

- ### Database (PostgreSQL)
- ### App (Django)

- ## Network connectivity

- ### Set depends_on on app service to start db first
- ### Docker Compose create a network
- ### The app service can use db hostname

- ## Volumes
- ### Persistent data
- ### Maps directory in container to local machine
- ###
