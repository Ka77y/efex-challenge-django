# efex-challenge-django

# Django Project

This project is an example API built with Django and Django Rest Framework. Below are the steps to set up and run the project.

## Prerequisites

Make sure you have the following installed on your system:

- [Python 3.x](https://www.python.org/downloads/)
- [Pip](https://pip.pypa.io/en/stable/) (Python package manager)
- [Django](https://www.djangoproject.com/) and [Django Rest Framework](https://www.django-rest-framework.org/)

## Installation

### 1. Clone the repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/Ka77y/efex-challenge-django.git
cd efex-challenge-django
```

### 2. Create a virtual environment

It is recommended to create a virtual environment to manage the project's dependencies. You can use `venv` (included in Python 3):

```bash
python -m venv venv
```

Activate the virtual environment:

On Windows:

```bash
venv\Scripts\activate
```
On macOS/Linux:

```bash
source venv/bin/activate
```

### 3. Install dependencies

Once inside the virtual environment, install the project dependencies with the following command:

```bash
pip install -r requirements.txt
```

### 4. Start the development server

To start the development server, run:
```bash
python manage.py runserver
```