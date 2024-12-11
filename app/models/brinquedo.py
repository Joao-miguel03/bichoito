from flask_sqlalchemy import SQLAlchemy
from app.__init__ import db

class Brinquedo (db.Model):
    __tablename__ = 'brinquedo'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    nome = db.Column(db.String(30), nullable = False)
    descricao = db.Column(db.String(50), nullable = False)
    preco = db.Column(db.Float, nullable = False)
    disponivel = db.Column(db.Boolean, nullable = False)
    imagem  = db.Column(db.LargeBinary, nullable = True)

