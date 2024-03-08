# uvicorn app.main:app
# app.main is the file main.py in the app folder.
## :app indicates the instance app=FastAPI() below.

from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

