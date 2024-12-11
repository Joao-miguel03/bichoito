from flask_sqlalchemy import SQLAlchemy
from app.__init__ import db

class Duvida (db.Model):
    __tablename__ = 'duvida' 
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    titulo = db.Column(db.String(80), nullable = False)
    descricao = db.Column(db.String(80), nullable = True)
    id_usuario =db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable = False)

    usuario = db.relationship('Usuario', backref='duvida', lazy=True)


    
