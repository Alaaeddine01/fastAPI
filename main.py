from fastapi import FastAPI
from books import BOOKS

app = FastAPI()

# uvicorn main:app --reload


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/api/{dynamic_param}")
async def hello(dynamic_param):
    return {'dynamic_param':dynamic_param}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
@app.get("/books")
async def get_all_books():
    return BOOKS

@app.get("/api")
async def first_api():
    return {"name":"alaa"}

