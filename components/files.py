from components.constants import BOOKS
import os
import re

class Verse:
  def __init__(self, number, text = ""):
    self.number = number
    self.text = text
  
  def set_text(self, text):
    self.text = text
  
  def get_text(self):
    return self.text
  
  def __repr__(self):
    return f"<Verse {str(self.number)}: {self.text}>"

class Chapter:
  def __init__(self, number, verses: dict[int, Verse] = {}):
    self.number = number
    self.verses = verses
  
  def set_verses(self, verses: dict[int, Verse] = {}):
    self.verses = verses
  
  def get_verses(self):
    return self.verses
  
  def add_verse(self, number, verse:Verse):
    self.verses[number] = verse
  
  def __repr__(self):
    return f"<Chapter {self.number} with {len(self.verses)} verses>"

class Book:
  def __init__(self, number, chapters: dict[int, Chapter] = {}):
    self.number = number
    self.chapters = chapters
  
  def set_chapters(self, chapters:  dict[int, Chapter] = {}):
    self.chapters = chapters
  
  def get_chapters(self):
    return self.chapters
  
  def add_chapter(self, number, chapter:Chapter):
    self.chapters[number] = chapter
  
  def __repr__(self):
    return f"<Book: \"{BOOKS[self.number]}\" with {len(self.chapters)} chapters>"

def get_filename(book_index):
  return BOOKS[book_index] + ".txt"

def get_book_contents(filename):
  
  with open(os.path.join("data", filename), "r") as f:
    contents = f.read().strip().split("\n")[1:]
  
  return contents

def process_contents(book_index, contents) -> Book:
  chapters = {}
  
  current_chapter = 1
  chapter = Chapter(current_chapter)
  for verse in contents:
    verse_number = re.search(':(.*)]', verse).group(1) # type:ignore
    new_verse = Verse(verse_number, "]".join(verse.split("]")[1:]))
    
    #print(verse.split(":")[0][1:])
    if int(verse.split(":")[0][1:]) != current_chapter:
      chapters[current_chapter] = chapter
      current_chapter += 1
      chapter = Chapter(current_chapter, verses = {})
    
    chapter.add_verse(verse_number, new_verse)
    
  chapters[current_chapter] = chapter
  
  return Book(book_index, chapters)

def process(book_index) -> Book:
  filename = get_filename(book_index)
  contents = get_book_contents(filename)
  return process_contents(book_index, contents)

def get():
  return [process(book) for book in range(len(BOOKS))]