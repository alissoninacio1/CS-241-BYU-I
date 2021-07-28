
class Person:
   def __init__(self):
      self.name = "anonymous"
      self.year = "unknown"

   
   def display(self):
      print(f"{self.name} (b. {self.year})")

class Book:

   def __init__(self):
      self.title = "untitled"
      self.author = Person()
      self.publisher = "unpublished"

   def display(self):
      print(self.title)
      print("Publisher:")
      print(self.publisher)
      print("Author:")
      self.author.display() 


def main():
   book = Book()
   book.display()
   print()
   print("Please enter the following:")
   book.author.name = input("Name: ")
   book.author.year = input("Year: ")
   book.title = input("Title: ")
   book.publisher = input("Publisher: ")
   print()
   book.display() 

if __name__ == "__main__":
   main()
