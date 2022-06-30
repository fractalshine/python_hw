import json


class BooksDAO:

    def get_all(self):
        """
        Загружает книжки из файла
        """
        with open("books.json", "r", encoding="utf-8") as file:
            books = json.load(file)
        return books

    def get_by_id(self, book_id):
        """
            Получает
            :param book_id: id книги
            """
        books = self.get_all()
        for book in books:
            if book["pk"] == book_id:
                return book


books_dao = BooksDAO()

books_all = books_dao.get_all()
books_by_id = books_dao.get_by_id(2)

print(books_by_id)
