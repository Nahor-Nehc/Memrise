import random as rd
import os
from components.constants import BOOKS
from components.files import process

def standardise_books_input(books:tuple[str, ...]):
  """
  This function takes the list of inputted books and converts any names into the index
  """
  
  # method
  # new_books = []
  # for book in books:
  #   if book.isnumeric():
  #     new_books.append(int(book))
  #   else:
  #     new_books.append(BOOKS.index(book))
  
  return [int(book) if book.isnumeric() else BOOKS.index(book) for book in books]

def check_books_input(books:tuple[str, ...]):
  """returns all books if no books are provided"""
  book = BOOKS if not books else list(books)
  return book

def rand_book(*books:str):
  """
  returns a random book of:
    - all the books if no args are provided
    - the books provided as a sequence of args
  
  input books as full name of book OR the index in BOOKS
  """
  
  books = check_books_input(books)
  return rd.choice(books)

def rand_chapter(*books:str):
  """
  returns a random chapter of:
    - a random book if no args are provided
    - a random book out of the books provided as a sequence of args
  
  input books as full name of book OR the index in BOOKS
  """
  
  book = rand_book(books)
  return rd.choice()
  
def rand_verse(book, chapter):
  """
  returns a random verse of a random chapter of:
    - a random book if no args are provided
    - a random book out of the books provided as a sequence of args
  
  input books as full name of book OR the index in BOOKS
  """