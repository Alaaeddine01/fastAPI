from typing import Optional

from fastapi import FastAPI, Body, Path
from pydantic import BaseModel, Field
app = FastAPI()

class Book:
    id:int
    title:str
    author:str
    price:float
    published_date:int

    def __init__(self,id,title,author,price,published_date):
        self.id = id
        self.title = title
        self.author = author
        self.price = price
        self.published_date = published_date

class BookRequest(BaseModel):
    id: Optional[int]=Field(description='id is not needed for create',default=None)
    title: str = Field(min_length=3)
    author: str = Field(min_length=3)
    price: float = Field(gt=0,lt=100)
    published_date:int = Field(gt=2020)






BOOKS=[
    Book(1000,'java 17','alaa',23.00,2021),
Book(2000,'java 8','rachid',21.00,2022),
Book(3000,'python','alaa eddine',23.00,2023 ),
Book(4000,'docker','rachid',26.00,2024),
]

@app.get("/api/books")
async def read_all():
    return BOOKS

@app.post("/api/create-book")
async def create_book(book:BookRequest):

    new_book = Book(**book.model_dump())

    BOOKS.append(find_book_id(new_book))

@app.get("/api/books/{book_id}")
async def read_book_by_id(book_id:int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book
        break

@app.get("/api/books/")
async def read_book_by_price(price:float):
    books_returned = []
    for book in BOOKS:
        if book.price == price:
            books_returned.append(book)
    return books_returned
@app.put("/api/books/update-book")
async def update_book(book:BookRequest):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i]=book

@app.delete("/api/book/{id}")
async def delete_book_by_id(id:int=Path(gt=0)):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == id:
            BOOKS.pop(i)
            break

@app.get("/api/publish/")
async def filter_by_published_date(published_date:int):
    books_returned = []
    for book in BOOKS:
        if book.published_date == published_date:
            books_returned.append(book)
    return books_returned





#give automatically books id for book objects
def find_book_id(book : Book):
    book.id = 1 if len(BOOKS)==0 else BOOKS[-1].id + 1
    return book






















