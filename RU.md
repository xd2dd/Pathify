# Pathify ⭐

**Pathify** - это легкий и гибкий фреймворк для создания внутренних API-интерфейсов с использованием FastAPI. Вдохновленный Next.js routing, он позволяет легко организовывать и динамически загружать маршруты, создавая файлы Python в структуре каталогов. С помощью **Pathify** создавать маршруты API так же просто, как добавлять новые файлы Python в соответствующие папки.

---

⚠️ **Дисклеймер** ⚠️

**Этот проект является обучающей игрушкой и предназначен для ознакомления с основными концепциями и экспериментами.**
Он **не предназначен для использования в производственной среде** и **не соответствует необходимому уровню безопасности, производительности или отказоустойчивости**.

Используйте этот код на свой страх и риск. Для ваших проектов рекомендуется использовать ** проверенные фреймворки и библиотеки**.

---

### Особенности

- **Динамическая загрузка маршрутов**: Автоматически загружает маршруты из структуры каталогов.
- **Простая параметризация URL-адресов**: Поддерживает динамические параметры URL-адресов для простого создания RESTful API.
- **Простая поддержка HTTP-методов**: Простое определение HTTP-методов (`GET`, `POST`) в файлах Python.

### Установка

Вы можете установить **Pathify** из PyPI с помощью `pip`:

```bash
pip install pathifyapi
```

### Использование
Создаем GET / route:

```python
# routers/get.py
def get():
    return {"message": "Привет, Мир!"}
```
После запуска сервера маршрут GET / будет доступен по адресу http://localhost:8000/ и вернет {"message": "Привет, Мир!"}.

Создайте маршрут GET /hello/{name}:

```python
# routers/hello/{name}.py
def get(name: str):
    return {"message": f"Привет, {имя}!"}
```

### Пример структуры проекта

```
project/
├── app.py
└── routers/
    ├── get.py
    ├── hello/
    │ ├── {name}.ру
    └──users/
        ├── get.ру
        └── {id}/
            └── post.py
```

### Пример приложения FastAPI

```python
# app.py
from pathify import Pathify

pathify = Pathify(routers_dir="routers")

app = pathify.get_app()
```

Для начала используйте uvicorn:

```Приложение bash
uvicorn app:app --reload
```
