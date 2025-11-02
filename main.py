from fastapi import FastAPI, HTTPException
import random
import json
import os



app = FastAPI()


BOOKS_FILE = "books.json"

DATABASE_BOOKS = [
    "Harry Potter",
    "Marco Aurelio",
    "DSA basic"
]


# Verifica se existe o arquivo json
if os.path.exists(BOOKS_FILE):
    # carrega o arquivo .json para ser usado como leitura
    with open (BOOKS_FILE, "r") as f:
        DATABASE_BOOKS = json.load(f)



# endpoint para retorno da primeira mensagem com Python FastAPI
@app.get("/")
async def root():
    return {"message":"primeiro GET python!"}


# endpoint para retornar os livros da lista
@app.get("/books")
async def books():
    return DATABASE_BOOKS


# endpoint para buscar um livro pelo index
@app.get("/book/{index}")
async def book_index(index: int):
    if index < 0 or index > len(DATABASE_BOOKS):
        raise HTTPException(404, "Not Found book in list.")
    else:
        return { "Book" : DATABASE_BOOKS[index]}


# endpoint retorna livros de forma aleátorio
@app.get("/book-random")
async def book_randon():
    return {"Book": random.choice(DATABASE_BOOKS)}

@app.post("/add-book")
async def add_book(book: str):
    DATABASE_BOOKS.append(book)
    
    # adiciona o livro dentro do arquivo JSON
    with open (BOOKS_FILE, "w") as f:
        json.dump(DATABASE_BOOKS, f)    
            
    return {"message": f'Book {book} foi adicionado'}