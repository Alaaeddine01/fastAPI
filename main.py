from fastapi import FastAPI, Body
from books import BOOKS

app = FastAPI()

# uvicorn main:app --reload
@app.get("/api/books")
async def get_all_books():
    return BOOKS
@app.get("/api/test/mybook")
async def test_path_param():
    return {'static_param':'static parameter !'}
@app.get("/api/test/{dynamic_param}")
async def test_path_param(dynamic_param):
    return {'dynamic_param':dynamic_param}
@app.get("/api/books/{book_title}")
async def get_book_by_title(book_title:str):
    for book in BOOKS:
        if book.get('title').casefold()==book_title.casefold():
            return book

@app.get("/api/books/")
async def read_by_category(category:str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold()==category.casefold():
            books_to_return.append(book)
    return books_to_return

@app.get("/api/books/{author}/")
async def read_by_category_author(author:str,category:str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold()==author.casefold() and \
            book.get('category').casefold()== category.casefold():
            books_to_return.append(book)
    return books_to_return

@app.post("/api/books/creat-book")
async def add_books(new_book=Body()):
    BOOKS.append(new_book)



