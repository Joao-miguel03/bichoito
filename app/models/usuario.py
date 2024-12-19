from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from app.__init__ import app, db

class Usuario(UserMixin, db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(30), unique = True, nullable = False)
    senha = db.Column(db.String(20), nullable = False)
    nome = db.Column(db.String(30), nullable=False)
    foto_perfil = db.Column(db.LargeBinary, nullable = True)
    tem_carteira = db.Column(db.Boolean, nullable = True)