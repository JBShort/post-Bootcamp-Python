from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users;"
        users_from_db = connectToMySQL("users_schema").query_db(query)

        users_list = []
        for user in users_from_db:
            users_list.append(cls(user))
        
        return users

    @classmethod
    def get_one_user(cls, data):
        query = "SELECT * FROM users;"
        results = connectToMySQL("users_schema").query_db(query, data)

        users_obj = cls()

        return users_obj

    @classmethod
    def create(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(fname)s, %(lname)s, %(email)s, NOW(), NOW());"

        users_id = connectToMySQL("users_schema").query_db(query, data)

        return users_id

    
    @classmethod
    def delete_user(cls, data):
        query = "DELETE FROM dogs WHERE id = %(id)s"
        connectToMySQL("users_schema").query_db(query, data)

    
    @classmethod
    def update_user(cls, data):
        query = "UPDATE users SET first_name = %(fname)s, last_name = %(lname)s, email = %(email)s, updated_at = NOW() WHERE id = %(id)s"
        results = connectToMySQL("users_schema").query_db(query, data)

        return results