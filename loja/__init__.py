from flask import Flask, current_app, request
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///store.db"
app.config['SECRET_KEY'] = 'abcd'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
#db.create_all()

from loja.admin import rotas




