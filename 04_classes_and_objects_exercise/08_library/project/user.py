class User:
    def __init__(self, user_id: int, username: str):
        user_id = user_id
        username = username
        books = []

    def info(self):
        sorted_books = sorted(books)
        return f'{", ".join(book for book in sorted_books)}'

    def __str__(self):
        return f'{user_id}, {username}, {books}'