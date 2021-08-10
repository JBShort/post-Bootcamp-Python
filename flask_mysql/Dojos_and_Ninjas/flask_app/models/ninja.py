from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.dojo_id = data['dojo_id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    

    @classmethod
    def get_all_ninjas(cls, data):
        query = "SELECT * FROM ninjas WHERE dojo_id = %(dojo_id)s"
        ninjas_from_db = connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)

        all_ninjas = []

        for ninjas in ninjas_from_db:
            all_ninjas.append(cls(ninjas))

        return all_ninjas


    @classmethod
    def create(cls, data):
        query = "INSERT INTO ninjas (dojo_id, first_name, last_name, age, created_at, updated_at) VALUES (%(dojo_id)s, %(first_name)s, %(last_name)s, %(age)s, NOW(), NOW());"
        new_ninjas = connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)

        return new_ninjas