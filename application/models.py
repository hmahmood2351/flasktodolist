from application import db

#defining schema for database
# table-todo, in database 
# id pk
# name
# description
# due date
# status

class Todo(db.Model):
    noteid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    description = db.Column(db.String(100))
    duedate = db.Column(db.DateTime)
    status = db.Column(db.String(40))