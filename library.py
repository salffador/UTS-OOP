class User:
    def __init__(self, user_id, password):
        self._user_id = user_id
        self._password = password

    def login(self, user_id, password):
        if user_id == self._user_id and password == self._password:
            print(f"Welcome, User {self._user_id}!")
            return True
        else:
            print("Invalid user_id or password.")
            return False

    def get_user_id(self):
        return self._user_id

class Library(User):
    def __init__(self, user_id, password, library_name):
        super().__init__(user_id, password)
        self.library_name = library_name
        self.books = {}  # Dictionary to store book title and quantities
        self.loan_requests = []  # List to store loan requests

    def add_book(self, title, quantity):
        if title in self.books:
            self.books[title] += quantity
        else:
            self.books[title] = quantity
        print(f"{quantity} copies of '{title}' added to the library.")

    def request_book_loan(self, student_id, book_title):
        if book_title in self.books and self.books[book_title] > 0:
            self.loan_requests.append((student_id, book_title))
            print(f"Loan request for '{book_title}' by student {student_id} accepted.")
        else:
            print(f"Book '{book_title}' is not available for loan.")

    def approve_loan(self):
        if not self.loan_requests:
            print("No pending loan requests.")
            return
        student_id, book_title = self.loan_requests.pop(0)
        self.books[book_title] -= 1
        print(f"Loan approved for student {student_id} for the book '{book_title}'.")

    def check_book_availability(self, title):
        if title in self.books and self.books[title] > 0:
            print(f"'{title}' is available with {self.books[title]} copies remaining.")
        else:
            print(f"'{title}' is not available.")

# Example usage:
library = Library(5, "lib123", "Main Campus Library")
library.login(5, "lib123")
library.add_book("Python Programming", 3)
library.request_book_loan("422023029", "Python Programming")
library.approve_loan()
library.check_book_availability("Python Programming")
