from components.constants import BOOKS
import os

class Verse:
  def __init__(self, number, text = ""):
    self.number = number
    self.text = text
  
  def set_text(self, text):
    self.text = text
  
  def get_text(self):
    return self.text

class Chapter:
  def __init__(self, number, verses: list[Verse] = []):
    self.number = number
    self.verses = verses
  
  def set_verses(self, verses: list[Verse] = []):
    self.verses = verses
  
  def get_verses(self):
    return self.verses

  def append(self, verse: Verse):
    self.verses.append(verse)
  
  def 

class Book:
  def __init__(self, name, chapters: list[Chapter] = []):
    self.name = name
    self.chapters = chapters
  
  def set_chapters(self, chapters: list[Chapter] = []):
    self.chapters = chapters
  
  def get_chapters(self):
    return self.chapters

def get_filename(book_index):
  return BOOKS[book_index] + ".txt"

def get_book_contents(filename):
  
  with open(os.path.join("data", filename), "r") as f:
    contents = f.read().strip().split("\n")
  
  return contents

def process_contents(contents) -> Book:
  chapters = Chapters()
  for verse in contents:
    pass

def process(book_index):
  filename = get_filename(book_index)
  contents = get_book_contents(filename)
  contents = process_contents(contents)