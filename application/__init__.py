from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1:3306/todolist'
app.config['SECRET_KEY'] = 'randomsecuritykeytobeexportedwithenv'

db = SQLAlchemy(app)

import application.routes