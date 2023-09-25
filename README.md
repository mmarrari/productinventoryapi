# Product Inventory API

An API built with Django Rest Framework to manage and query a product inventory.

## 📚Table of Contents

- [📝Description](#description)
- [🛠Technologies Used](#technologies-used)
- [📊System Sequence Diagram](#system-sequence-diagram)
- [🔍Usage](#usage)
  - [Query Parameters](#query-parameters)
  - [Examples of Requests](#examples-of-requests)
- [🚀Setup and Installation](#setup-and-installation)
  - [Setting Environment Variables (Optional)](#setting-environment-variables-optional)
  - [Installation using Pipenv](#installation-using-pipenv)
  - [Installation using Poetry](#installation-using-poetry)
  - [Installation using virtualenv and pip](#installation-using-virtualenv-and-pip)
  - [Installation using docker-compose](#installation-using-docker-compose)
  - [Installation using Docker alone (without docker-compose)](#installation-using-docker-alone-without-docker-compose)
- [🧪Testing the API](#🧪testing-the-api)
  - [Testing in a Pipenv Environment](#testing-in-a-pipenv-environment)
  - [Testing in a Poetry Environment](#testing-in-a-poetry-environment)
  - [Testing in a virtualenv Environment](#testing-in-a-virtualenv-environment)
  - [Testing in a docker-compose Environment](#testing-in-a-docker-compose-environment)
  - [Testing in a Docker Environment (without docker-compose)](#testing-in-a-docker-environment-without-docker-compose)
- [🔗Useful Links](#useful-links)


## 📝Description

The Product Inventory API allows users to query products based on various search parameters. Whether you're looking for products by name, price range, or category, our API delivers fast and accurate results.

## 🛠Technologies Used

- **Programming Language**: Python 3.x
- **Web Framework**: Django 4.x
- **API Framework**: Django Rest Framework
- **Database**: SQLite


## 📊System Sequence Diagram

Below is a sequence diagram that illustrates the communication process between the client making a GET request, the Django server, and the SQLite database. This visual representation provides a clear overview of how different components interact during a typical query to our API.

![sequence](./images/django-sequence.svg)

## 🔍Usage
Users can fetch a list of products based on various filter criteria, ensuring that the returned data is both relevant and concise.
Endpoint:
```http
GET /products/
```
### Query Parameters:
* name: Perform a case-insensitive search to filter products by name.
**Example**: name=laptop would match products named "Laptop", "laptop", "Ultra-thin Laptop", etc.

* min_price and max_price: Define a price range to filter products within the specified boundaries.
**Example**: min_price=100&max_price=500 would match products priced between 100 and 500 units inclusive.

* category: Filter products based on their category. The available categories are Electronics, Clothing, and Food.
**Example**: category=Electronics would match products categorized as Electronics.

📝 Note: Multiple categories can be provided by repeating the parameter. For example, category=Electronics&category=Clothing.

### Examples of Requests:
To fetch all products:
```http
GET /products/
```
To fetch products where the name contains "shirt":
```http
GET /products/?name=shirt
```
To fetch products in the "Electronics" category priced between 100 and 500:
```http
GET /products/?category=Electronics&min_price=100&max_price=500
```
For paginated results, you can use the page and page_size parameters.
To fetch the second page of products with a page_size of 5:
```http
GET /products/?page=2&page_size=5
```
Combining various parameters:
To fetch the second page of products in the "Clothing" category with names containing "shirt", priced between 10 and 1000, and with a page size of 5:
```http
GET /products/?name=shirt&min_price=10&max_price=1000&category=Clothing&page=2&page_size=5
```

## 🚀Setup and Installation
Before starting the installation process with your preferred package manager, you have the option to configure certain environment variables. However, setting these environment variables is not mandatory. If you choose not to set them, default values will be used.

### Setting Environment Variables (Optional)
`DJANGO_ADMIN_USER`: This specifies the username for the Django admin. If not set, the default will be admindj.

```bash
export DJANGO_ADMIN_USER="your_desired_admin_username"
```

`DJANGO_ADMIN_PASS`: This specifies the password for the Django admin. If not set, the default will be passdj.

```bash
export DJANGO_ADMIN_PASS="your_desired_admin_password"
```
With the environment variables set (or relying on the default values), proceed with one of the following installation methods based on your preference:

### Installation using Pipenv
In the root directory of the project, install the dependencies using Pipenv:
```bash
pipenv install
```
Once the dependencies are installed, execute the setup command:
```bash
pipenv run python product_inventory_api/manage.py setupproject
```
### Installation using Poetry
In the root directory of the project, install the dependencies using Poetry:
```bash
poetry install
```
From the root directory of the project, execute the setup command:
```bash
poetry run python product_inventory_api/manage.py setupproject
```
### Installation using virtualenv and pip
In the root directory of the project, create a new virtual environment:
```bash
virtualenv venv
```
Activate the virtual environment:
```bash
source venv/bin/activate
```
Once the virtual environment is activated, install the required packages:
```bash
pip install -r requirements.txt
```
And finally, execute the setup command:
```bash
python product_inventory_api/manage.py setupproject
```

### Installation using docker-compose
Build the Docker image and spin up the container:

```bash
docker-compose up --build
```
#### Execute Django-specific commands (if necessary)
Because web is the name of the service defined in your docker-compose.yml running the Django app. You need first run in daemond mode:
```bash
docker-compose up -d
```
and then you could run:
```bash
docker-compose exec web python manage.py check
```
#### Stopping and removing containers:
When you're done, you can stop and remove the containers with:
```bash
docker-compose down
```
and the image
```bash
docker rmi web
```

### Installation using Docker alone (without docker-compose)
In the root directory of the project, execute:
```bash
docker build -t web .
```
and run with:
```bash
docker run -p 8000:8000 web
```
#### Execute Django-specific commands (if necessary)
Because web is the name of the service defined in your docker run command (--name web)  running the Django app. You need first run in daemond mode:
```bash
docker run -d --name web -p 8000:8000 web
```
and then you could run:
```bash
docker exec -it web python manage.py check
```
#### Stopping and removing containers:
When you're done, you can stop and remove the containers with:
```bash
docker stop web
docker rm web
```
and the image
```bash
docker rmi web
```

## 🧪Testing the API
Below are the instructions to run tests for the Product Inventory API across various environments and setups.

### Testing in a Pipenv Environment
If you have set up your project using Pipenv, you can run (root directory) the tests with:
```bash
pipenv run python product_inventory_api/manage.py test product_service
```
### Testing in a Poetry Environment
If you have set up your project using Poetry, you can run (root directory) the tests with:
```bash
poetry run python product_inventory_api/manage.py test product_service
```
### Testing in a virtualenv Environment
If you've set up your project with virtualenv, ensure you're in the root directory and that the environment is properly set up and activated. Then, execute the tests as follows:
```bash
python product_inventory_api/manage.py test product_service
```
### Testing in a docker-compose Environment
When running your project using docker-compose, first ensure the containers are up. Then, execute the tests in the web container:
```bash
docker-compose exec web python manage.py test product_service
```
### Testing in a Docker Environment (without docker-compose)
If you're using Docker standalone, first make sure your container is up and running. If you've started the container with the name "web" as previously detailed, you can execute the following:
```bash
docker exec -it web python manage.py test product_service
```

## 🔗Useful Links
Here is a collection of helpful links related to the tools and technologies used in this API:

- **Poetry**: A tool for dependency management and packaging in Python.
  - [Official Poetry Documentation](https://python-poetry.org/docs/)

- **Pipenv**: A tool for managing dependencies and virtual environments.
  - [Official Pipenv Documentation](https://pipenv.pypa.io/en/latest/)

- **Docker**: A platform for developing, shipping, and running applications in containers.
  - [Official Docker Documentation](https://docs.docker.com/)

- **Docker Compose**: A tool for defining and running multi-container Docker applications.
  - [Official Docker Compose Documentation](https://docs.docker.com/compose/)

- **Virtualenv**: A tool for creating independent virtual environments in Python.
  - [Official Virtualenv Documentation](https://virtualenv.pypa.io/en/latest/)

- **Django**: A high-level web framework based on Python.
  - [Official Django Documentation](https://docs.djangoproject.com/)

- **Django Rest Framework**: A powerful and flexible toolkit for building web APIs.
  - [Official Django Rest Framework Documentation](https://www.django-rest-framework.org/)

- **django-filter**: A library to ease adding filters to your views.
  - [Official django-filter Documentation](https://django-filter.readthedocs.io/en/stable/)
