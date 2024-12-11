from flask_sqlalchemy import SQLAlchemy
from app.__init__ import db

class Carteira(db.Model):
    __tablename__ = 'carteira'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable = False)
    CPF = db.Column(db.String(30), unique = True, nullable = False)
    senha_cartao = db.Column(db.String(20), nullable = False)
    num_cartao = db.Column(db.Integer, nullable=False)
    saldo = db.Column(db.Float, nullable = True)

    usuario = db.relationship('Usuario', backref = 'carteira', lazy = True)