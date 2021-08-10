from flask_app.config.mysqlconnection import connectToMySQL
from ..models import author

class Book:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.authors = []

    
    @classmethod
    def get_all_books(cls):
        query = "SELECT * FROM books;"
        results = connectToMySQL("books_schema").query_db(query)

        return results

    
    @classmethod
    def create(cls, data):
        query = "INSERT INTO books (title, num_of_pages, created_at, updated_at) VALUES (%(title)s, %(num_of_pages)s, NOW(), NOW());"
        results = connectToMySQL("books_schema").query_db(query, data)

        return results

    
    @classmethod
    def books_with_favorites_with_authors(cls, data):
        query = "SELECT * FROM books LEFT JOIN favorite_books ON books.id = favorite_books.book_id LEFT JOIN authors ON favorite_books.author_id = authors.id;"
        results = connectToMySQL("books_schema").query_db(query, data)

        books = cls(results[0])

        for row in results:
            data = {
                "id": row['id'],
                "favorite_book_by_id": row['favorite_books.id'],
                "book_title": row['title'],
                "num_of_pages": row['num_of_pages']
            }
            books.authors.append(Author(data))
        
        return books