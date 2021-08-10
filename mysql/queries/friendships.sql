INSERT INTO users (first_name, last_name, created_at, updated_at)
VALUES ("Amy", "Giver", NOW(), NOW()),
	("Eli", "Byers", NOW(), NOW()),
    ("Marky", "Mark", NOW(), NOW());
    
    
INSERT INTO users (first_name, last_name, created_at, updated_at)
VALUES ("Big", "Bird", NOW(), NOW()),
	("Kermit", "The Frog", NOW(), NOW()),
    ("Who", "Dis", NOW(), NOW());
    
    
INSERT INTO friendship (id, user_id, friend_id, created_at, updated_at)
VALUES (1, 1, 2, NOW(), NOW()),
	(2, 1, 4, NOW(), NOW()),
    (3, 1, 6, NOW(), NOW());
    
    
INSERT INTO friendship (id, user_id, friend_id, created_at, updated_at)
VALUES (4, 2, 1, NOW(), NOW()),
	(5, 2, 3, NOW(), NOW()),
    (6, 2, 5, NOW(), NOW());
    
    
INSERT INTO friendship (id, user_id, friend_id, created_at, updated_at)
VALUES (4, 2, 1, NOW(), NOW()),
	(5, 2, 3, NOW(), NOW()),
    (6, 2, 5, NOW(), NOW());
    

INSERT INTO friendship (id, user_id, friend_id, created_at, updated_at)
VALUES (7, 3, 2, NOW(), NOW()),
	(8, 3, 5, NOW(), NOW());
    

INSERT INTO friendship (id, user_id, friend_id, created_at, updated_at)
VALUES (9, 4, 3, NOW(), NOW());


INSERT INTO friendship (id, user_id, friend_id, created_at, updated_at)
VALUES (10, 5, 1, NOW(), NOW()),
	(11, 5, 6, NOW(), NOW());
    

INSERT INTO friendship (id, user_id, friend_id, created_at, updated_at)
VALUES (12, 6, 2, NOW(), NOW()),
	(13, 6, 3, NOW(), NOW());
    

SELECT users.first_name, users.last_name, user2.first_name as friend_first_name, user2.last_name as friend_last_name FROM users
JOIN friendship ON users.id = friendship.user_id
LEFT JOIN users as user2 ON user2.id = friendship.friend_id;