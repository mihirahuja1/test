class Book:
    def __init__(self, id, title, author, status="available"):
        self.id = id
        self.title = title
        self.author = author
        self.status = status

    def __str__(self):
        return f"{self.id}. {self.title} by {self.author} - {self.status}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def issue_book(self, id):
        for book in self.books:
            if book.id == id and book.status == "available":
                book.status = "issued"
                print(f"Book {book.title} has been issued!")
                return
        print("Book either not found or already issued.")

    def return_book(self, id):
        # TODO
        pass

    def display_books(self):
        for book in self.books:
            print(book)


def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add book")
        print("2. Issue book")
        print("3. Return book")
        print("4. Display all books")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            id = int(input("Enter book ID: "))
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            library.add_book(Book(id, title, author))

        elif choice == 2:
            id = int(input("Enter book ID to issue: "))
            library.issue_book(id)

        elif choice == 3:
            id = int(input("Enter book ID to return: "))
            library.return_book(id)

        elif choice == 4:
            library.display_books()

        elif choice == 5:
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
