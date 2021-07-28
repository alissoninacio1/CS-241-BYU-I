class Book:
    def __init__(self):
        self.title = ""
        self.author = ""
        self.publication_year = 0

    def prompt_book_info(self):
        self.title = input("Title: ")
        self.author = input("Author: ")
        self.publication_year = input("Publication Year: ")

    def display_book_info(self):
        print(f"{self.title} ({self.publication_year}) by {self.author}")

class TextBook(Book):
    def __init__(self):
        self.subject = ""

    def prompt_subject(self):
        self.subject = input("Subject: ")

    def display_subject(self):
        print(f"Subject: {self.subject}")

class PictureBook(Book):
    def __init__(self):
        self.illustrator = ""

    def prompt_illustrator(self):
        self.illustrator = input("Illustrator: ")

    def display_illustrator(self):
        print(f"Illustrated by {self.illustrator}")


def main():
    b = Book()
    t = TextBook()
    p = PictureBook()

    b.prompt_book_info()
    print()
    b.display_book_info()
    print()

    t.prompt_book_info()
    t.prompt_subject()
    print()
    t.display_book_info()
    t.display_subject()
    print()

    p.prompt_book_info()
    p.prompt_illustrator()
    print()
    p.display_book_info()
    p.display_illustrator()

if __name__ == "__main__":
    main()
