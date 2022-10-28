from project.user import User


class Library:
    def __init__(self):
        user_records = []
        books_available = {}
        rented_books = {}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User):
        if book_name in books_available[author]:
            user.books.append(book_name)
            books_available[author].remove(book_name)
            if user.username in rented_books:
                rented_books[user.username][book_name] = days_to_return
            else:
                rented_books[user.username] = {book_name: days_to_return}
            return f'{book_name} successfully rented for the next {days_to_return} days!'
        else:
            for name, v in rented_books.items():
                if book_name in v:
                    return f'The book "{book_name}" is already rented and will be available in {v[book_name]} days!'

    def return_book(self, author: str, book_name: str, user: User):
        if book_name in rented_books[user.username]:
            user.books.remove(book_name)
            del rented_books[user.username][book_name]
            books_available[author].append(book_name)
        else:
            return f"{user.username} doesn't have this book in his/her records!"
