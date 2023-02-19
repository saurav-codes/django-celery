from src.celery import app


@app.task()
def add(x, y):
    print(f"Adding {x} and {y} is {x + y}")