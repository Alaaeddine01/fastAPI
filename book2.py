from fastapi import FastAPI

app = FastAPI()

class Book:
    id:int
    title:str
    author:str
    price:float

    def __init__(self,id,title,author,price):
        self.id = id
        self.title = title
        self.author = author
        self.price = price

BOOKS=[]

@app.get("/api/books")
async def read_all():
    return BOOKS

