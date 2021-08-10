INSERT INTO authors (name, created_at, updated_at)
VALUES ("Jane Austen", NOW(), NOW()),
	("Emily Dickinson", NOW(), NOW()),
    ("Fyodor Dostoevsky", NOW(), NOW()),
    ("William Shakespear", NOW(), NOW()),
    ("Lau Tzu", NOW(), NOW());
    
    
INSERT INTO books (title, num_of_pages, created_at, updated_at)
VALUES ("C Sharp", 100, NOW(), NOW()),
	("Java", 100, NOW(), NOW()),
    ("Python", 100, NOW(), NOW()),
    ("PHP", 100, NOW(), NOW()),
    ("Ruby", 100, NOW(), NOW());
    
    
UPDATE books SET title = "C#" WHERE id = 1;


UPDATE authors SET name = "Bill" WHERE id = 4;


INSERT INTO favorite_books (id, book_id, author_id, created_at, updated_at)
VALUES (1, 1, 1, NOW(), NOW()),
	(2, 2, 1, NOW(), NOW());
    
    
INSERT INTO favorite_books (id, book_id, author_id, created_at, updated_at)
VALUES (3, 1, 2, NOW(), NOW()),
	(4, 2, 2, NOW(), NOW()),
    (5, 3, 2, NOW(), NOW());
    
    
INSERT INTO favorite_books (id, book_id, author_id, created_at, updated_at)
VALUES (6, 1, 3, NOW(), NOW()),
	(7, 2, 3, NOW(), NOW()),
    (8, 3, 3, NOW(), NOW()),
    (9, 4, 3, NOW(), NOW());
    
    
INSERT INTO favorite_books (id, book_id, author_id, created_at, updated_at)
VALUES (10, 1, 4, NOW(), NOW()),
	(11, 2, 4, NOW(), NOW()),
    (12, 3, 4, NOW(), NOW()),
    (13, 4, 4, NOW(), NOW()),
    (14, 5, 4, NOW(), NOW());
    
    
SELECT name from authors
JOIN favorite_books ON authors.id = favorite_books.author_id
WHERE book_id = 3;


DELETE FROM favorite_books WHERE book_id = 3 AND author_id = 1;


INSERT INTO favorite_books (id, book_id, author_id, created_at, updated_at)
VALUES (15, 2, 5, NOW(), NOW());


SELECT title from books
JOIN favorite_books ON books.id = favorite_books.book_id
WHERE author_id = 3;


SELECT name FROM authors
JOIN favorite_books ON authors.id = favorite_books.author_id
WHERE favorite_books.book_id = 5;