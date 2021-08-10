INSERT INTO dojos (name, created_at, updated_at)
VALUES ("San Jose", NOW(), NOW()),
	("Los Angeles", NOW(), NOW()),
    ("Clemency", NOW(), NOW());
    
    
    
DELETE FROM dojos WHERE id = 1;
DELETE FROM dojos WHERE id = 2;
DELETE FROM dojos WHERE id = 3;



INSERT INTO dojos (name, created_at, updated_at)
VALUES ("San Jose", NOW(), NOW()),
	("Los Angeles", NOW(), NOW()),
    ("Clemency", NOW(), NOW());
    
    
Select * From dojos;


INSERT INTO ninjas (dojo_id, first_name, last_name, age, created_at, updated_at)
VALUES (7, "Jeremi", "Short", 29, NOW(), NOW()),
	(8, "Ren", "Mehtos", 20, NOW(), NOW()),
    (9, "Esme", "Adel", 30, NOW(), NOW());
    
    
INSERT INTO ninjas (dojo_id, first_name, last_name, age, created_at, updated_at)
VALUES (7, "Ben", "Ken", 29, NOW(), NOW()),
	(8, "Grieve", "Us", 20, NOW(), NOW()),
    (9, "Emp", "Palp", 30, NOW(), NOW());
    

INSERT INTO ninjas (dojo_id, first_name, last_name, age, created_at, updated_at)
VALUES (7, "Ana", "Kin", 29, NOW(), NOW()),
	(8, "Pad", "Me", 20, NOW(), NOW()),
    (9, "Jar", "Jar", 30, NOW(), NOW());
    
    
SELECT * FROM ninjas WHERE dojo_id = 7;
SELECT * FROM ninjas WHERE dojo_id = 8;
SELECT * FROM ninjas WHERE dojo_id = 9;

SELECT * FROM dojos
JOIN ninjas ON dojos.id = ninjas.dojo_id
ORDER BY ninjas.id DESC LIMIT 1;