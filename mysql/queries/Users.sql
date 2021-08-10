INSERT INTO users (first_name, last_name, email, created_at, updated_at)
VALUES ("Jeremi", "Short", "jbshort@gmail.com", NOW(), NOW()),
	("Ren", "Methos", "renmenthos@gmail.com", NOW(), NOW()),
	("Esme", "Adel", "esmeAdel@gmail.com", NOW(), NOW());
    
SELECT * FROM users;

SELECT email FROM users WHERE id = 1;

SELECT * from users WHERE id = 3;

UPDATE users SET last_name = "Pancakes" WHERE id = 3;

DELETE FROM users WHERE id = 2;

SELECT * FROM users
ORDER BY first_name ASC;

SELECT * FROM users
ORDER BY first_name DESC;