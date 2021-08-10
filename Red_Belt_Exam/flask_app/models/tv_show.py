from flask import flash
from ..config.mysqlconnection import connectToMySQL
from ..models import user

class TV_show:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.network = data['network']
        self.release_date = data['release_date']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        if 'user' in data:
            self.user = data['user']

    
    @classmethod
    def get_all_tv_shows(cls):
        query = "SELECT *, DATE_FORMAT(release_date, '%M %w %Y') FROM tv_shows;"
        results = connectToMySQL("tv_shows_schema").query_db(query)

        all_tv_shows = []

        for tv_shows in results:
            all_tv_shows.append(cls(tv_shows))
        
        return all_tv_shows


    @classmethod
    def create(cls, data):
        query = "INSERT INTO tv_shows (user_id, title, network, release_date, description, created_at, updated_at) VALUES (%(user_id)s, %(title)s, %(network)s, %(release_date)s, %(description)s, NOW(), NOW());"
        results = connectToMySQL("tv_shows_schema").query_db(query, data)

        return results

    
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM tv_shows WHERE id = %(id)s;"
        results = connectToMySQL("tv_shows_schema").query_db(query, data)

        results_data = {
            "id": results[0]['id'],
            "title": results[0]['title'],
            "network": results[0]['network'],
            "release_date": results[0]['release_date'],
            "description": results[0]['description'],
            "created_at": results[0]['created_at'],
            "updated_at": results[0]['updated_at'],
            "user": user.User.get_by_id({"id": results[0]['user_id']})
            
        }

        return cls(results_data)


    @classmethod
    def update_tv_show(cls, data):
        query = "UPDATE tv_shows SET title = %(title)s, network = %(network)s, release_date = %(release_date)s, description = %(description)s, updated_at = NOW() WHERE id = %(id)s"

        tv_show_id = connectToMySQL("tv_shows_schema").query_db(query, data)

        return tv_show_id


    @classmethod
    def delete(cls, data):
        query = "DELETE FROM tv_shows WHERE id = %(id)s;"
        connectToMySQL("tv_shows_schema").query_db(query, data)


    @classmethod
    def get_user_with_tv_shows1(cls, data):
        query = "SELECT * FROM users LEFT JOIN tv_shows ON users.id = tv_shows.user_id WHERE users.id = %(id)s;"
        results = connectToMySQL("tv_shows_schema").query_db(query, data)

        user = cls(results[0])

        for row in results:
            data = {
                "id": row['tv_shows.id'],
                "user_id": row['user_id'],
                "title": row['title'],
                "network": row['network'],
                "release_date": row['release_Date'],
                "description": row['description'],
                "created_at": row['tv_shows.created_at'],
                "updated_at": row['tv_shows.updated_at'],
                "user": user.User.get_by_id({"id": results[0]['user_id']})
            }
            user.tv_shows.append(TV_show(data))
        
        return user


    @staticmethod
    def validator(post_data):
        is_valid = True

        if len(post_data['title']) < 1:
            flash("Title must not be empty.")
            is_valid = False
        
        if len(post_data['network']) < 2:
            flash("Network must be longer than 2 characters.")
            is_valid = False
        
        if len(post_data['release_date']) < 1:
            flash("Please select a release date.")
            is_valid = False
        
        if len(post_data['description']) < 1:
            flash("Please include a small description.")
            is_valid = False

        return is_valid