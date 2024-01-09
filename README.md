# WebWebWeb

VSCode extensions:

- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

## 1. Python

Install Python 3.12: https://www.python.org/downloads/

## 2. Virtual environment

Create venv:

`python -m venv .venv`

Activate venv:

`.\.venv\Scripts\activate` (Windows)

Install deps:

`pip install -r ./requirements.txt`

## 3. Start server

`uvicorn main:app --reload`

Go to http://127.0.0.1:8000/docs and call `/auth/register`
