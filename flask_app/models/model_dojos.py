from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.model_ninjas import Ninja

class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at= data['updated_at']
        self.ninjas = []

    @classmethod
    def save(cls,data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        dojo_id = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        return dojo_id 

    
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM dojos;'
        dojos_from_db = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
      
        all_dojos =[]
        for dojo in dojos_from_db:
            all_dojos.append(cls(dojo))
        return all_dojos

    @classmethod
    def get_by_id(cls,data):
        query = 'SELECT * FROM dojos WHERE id = %(dojos_id)s;'
        mysql = connectToMySQL('dojos_and_ninjas_schema')	
        dojo = mysql.query_db(query,data) 
        return cls(dojo[0])

    @classmethod
    def get_dojos_with_ninjas(cls,data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        print(results)
        dojo = cls(results[0] )
        for row_from_db in results:
            
            data = {
                "id" : row_from_db["ninjas.id"],
                "first_name" : row_from_db["first_name"],
                "last_name" :  row_from_db["last_name"],
                "age" : row_from_db["age"],
                "created_at" : row_from_db["ninjas.created_at"],
                "updated_at" : row_from_db["ninjas.updated_at"]
            }
            dojo.ninjas.append(Ninja(data))
        return dojo 


"""
    @classmethod
    def update(cls,data):
        mysql = connectToMySQL('users')
        query = 'UPDATE users SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s WHERE id=%(id)s'
        return mysql.query_db(query,data)

    @classmethod
    def delete(cls,data):
        mysql = connectToMySQL('users')
        query = 'DELETE FROM users WHERE id=%(id)s'
        return mysql.query_db(query,data) """