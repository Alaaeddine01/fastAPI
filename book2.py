from typing import Optional

from fastapi import FastAPI, Body
from pydantic import BaseModel, Field
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

class BookRequest(BaseModel):
    id: Optional[int]=None
    title: str = Field(min_length=3)
    author: str = Field(min_length=3)
    price: float = Field(gt=0,lt=100)






BOOKS=[
    Book(1000,'java 17','alaa',23.00),
Book(2000,'java 8','rachid',21.00),
Book(3000,'python','alaa eddine',23.00),
Book(4000,'docker','rachid',26.00),
]

@app.get("/api/books")
async def read_all():
    return BOOKS

@app.post("/api/create-book")
async def create_book(book:BookRequest):

    new_book = Book(**book.model_dump())

    BOOKS.append(find_book_id(new_book))



#give automatically books id for book objects
def find_book_id(book : Book):
    book.id = 1 if len(BOOKS)==0 else BOOKS[-1].id + 1
    return book






















