from flask_app.config.mysqlconnection import connectToMySQL
from ..models import book

class Author:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.books = []

    @classmethod
    def get_all_authors(cls, data):
        query = "SELECT * FROM authors;"
        authors_from_db = connectToMySQL("books_schema").query_db(query)

        authors = []

        for author in authors_from_db:
            authors.append(cls(author))

        return authors
    

    @classmethod
    def get_one_author(cls, data):
        query = "SELECT * FROM authors WHERE id = %(id)s;"
        results = connectToMySQL("books_schema").query_db(query)

        authors = cls(results[0])

        return authors


    @classmethod
    def get_authors_with_favorites_with_books(cls, data):
        query = "SELECT * FROM authors LEFT JOIN favorite_books ON authors.id = favorite_books.author_id" \
            "LEFT JOIN books ON favorite_books.book_id = books.id;"
        results = connectToMySQL("books_schema").query_db(query, data)

        author = cls(results[0])

        for row in results:
            row_data = {
                "id": row['books.id'],
                "title": row['title'],
                "num_of_pages": row['num_of_pages'],
                'created_at': row['books.created_at'],
                'updated_at': row['books.updated_at']
            }
            authors.books.append(book.Book(row_data))

        return author


    @classmethod
    def create(cls, data):
        query = "INSERT INTO authors (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"

        results = connectToMySQL("books_schema").query_db(query, data)

        return results