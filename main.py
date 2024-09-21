from utils import User, Librarian, Member, Book

class LibraryManager:
    def __init__(self):
        self.books: List[Book] = []
        self.users: List[User] = []

    @classmethod
    def get_total_books(cls) -> int:
        return len(cls.books)

    @classmethod
    def get_total_users(cls) -> int:
        return len(cls.users)

    def add_book(self, book: Book) -> None:
        self.books.append(book)
        self._write_books_to_file()

    def update_book(self, book_id: int, title: str, author: str) -> None:
        for book in self.books:
            if book.book_id == book_id:
                book.title = title
                book.author = author
                self._write_books_to_file()
                return
        print("Book not found")

    def delete_book(self, book_id: int) -> None:
        self.books = [book for book in self.books if book.book_id != book_id]
        self._write_books_to_file()

    def add_user(self, user: User) -> None:
        self.users.append(user)
        self._write_users_to_file()

    def borrow_book(self, book_id: int, user: Member) -> None:
        for book in self.books:
            if book.book_id == book_id:
                if book.availability:
                    book.availability = False
                    self._write_books_to_file()
                    print(f"Book '{book.title}' borrowed by {user.name}")
                    return
                print("Book is not available")
                return
        print("Book not found")

    def return_book(self, book_id: int) -> None:
        for book in self.books:
            if book.book_id == book_id:
                book.availability = True
                self._write_books_to_file()
                print(f"Book '{book.title}' returned")
                return
        print("Book not found")

    def _write_books_to_file(self) -> None:
        try:
            with open("books.txt", "w") as file:
                for book in self.books:
                    file.write(f"{book.book_id},{book.title},{book.author},{int(book.availability)}\n")
        except IOError as e:
            print(f"Error writing to file: {e}")

    def _write_users_to_file(self) -> None:
        try:
            with open("users.txt", "w") as file:
                for user in self.users:
                    file.write(f"{user.user_id},{user.name},{user.email}\n")
        except IOError as e:
            print(f"Error writing to file: {e}")

    def _read_books_from_file(self) -> None:
        try:
            with open("books.txt", "r") as file:
                for line in file:
                    book_id, title, author, availability = line.strip().split(",")
                    self.books.append(Book(int(book_id), title, author, bool(int(availability))))
        except FileNotFoundError:
            pass
        except IOError as e:
            print(f"Error reading from file: {e}")

    def _read_users_from_file(self) -> None:
        try:
            with open("users.txt", "r") as file:
                for line in file:
                    user_id, name, email = line.strip().split(",")
                    self.users.append(User(int(user_id), name, email))
        except FileNotFoundError:
            pass
        except IOError as e:
            print(f"Error reading from file: {e}")

def __init__(self):
        super().__init__()
        self._read_books_from_file()
        self._read_users_from_file()

# Example usage
library_manager = LibraryManager()

# Add a new book
book = Book(1, "The Great Gatsby", "F. Scott Fitzgerald", True)
library_manager.add_book(book)

# Add a new librarian
librarian = Librarian(1, "John Doe", "johndoe@example.com")
library_manager.add_user(librarian)

# Add a new member
member = Member(2, "Jane Doe", "janedoe@example.com")
library_manager.add_user(member)

# Borrow a book
library_manager.borrow_book(1, member)

# Return a book
library_manager.return_book(1)

# List all books
for book in library_manager.books:
    print(f"Title: {book.title}, Author: {book.author}, Availability: {book.availability}")