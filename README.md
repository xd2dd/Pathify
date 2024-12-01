# Pathify ⭐

**Pathify** is a lightweight and flexible framework for building backend APIs with FastAPI. Inspired by Next.js routing, it allows you to easily organize and dynamically load routes by creating Python files in a directory structure. With **Pathify**, creating API routes is as simple as adding new Python files in corresponding folders.

---

⚠️ **Disclaimer** ⚠️

**This project is an educational toy and is intended for basic concepts and experiments.**
It is **not intended for use in a production environment** and does **not meet the necessary level of security, performance, or fault tolerance**.

Use this code at your own risk. For your projects, it is recommended to rely on **proven frameworks and libraries**.

---

### Features

- **Dynamic Route Loading**: Automatically loads routes from the directory structure.
- **Easy URL Parameterization**: Supports dynamic URL parameters for building RESTful APIs easily.
- **Simple HTTP Method Support**: Easily define HTTP methods (`GET`, `POST`) in Python files.

### Installation

You can install **Pathify** from PyPI via `pip`:

```bash
pip install pathifyapi
```

### Usage
Create a GET / route:

```python
# routers/get.py
def get():
    return {"message": "Hello, World!"}
```
After starting the server, the route GET / will be available at http://localhost:8000/ and will return {"message": "Hello, World!"}.

Create a GET /hello/{name} route:

```python
# routers/hello/{name}.py
def get(name: str):
    return {"message": f"Hello, {name}!"}
```

### Example project structure

```
project/
├── app.py
└── routers/
    ├── get.py
    ├── hello/
    │   ├── {name}.py
    └── users/
        ├── {id}.py
        └── {id}/
            └── post.py
```

### Example FastAPI application

```python
from pathify import Pathify

pathify = Pathify(routers_dir="routers")

app = pathify.get_app()
```

To get started use uvicorn:

```bash
uvicorn app:app --reload
```


Russian README.md [here](./RU.md)
