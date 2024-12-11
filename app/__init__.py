import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

projeto_dir = os.path.dirname(os.path.abspath(__file__))
database_file = f"sqlite:///{os.path.join(projeto_dir,"bichoito.db")}"

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)