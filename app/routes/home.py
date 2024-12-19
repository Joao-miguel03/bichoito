from flask import Blueprint, render_template, redirect, request, url_for, flash
from app.models.duvida import Duvida
from app.models.usuario import Usuario
from app.__init__ import db

homeBlueprint = Blueprint('home', __name__)

#rota inicial
@homeBlueprint.route('/', methods = ['GET'])
def home():
    return render_template('index.html')

@homeBlueprint.route('/sobrenos', methods = ['GET'])
def sobreNos():
    return render_template('sobreNos.html')

@homeBlueprint.route('/duvidas')
def duvidas():
    duvidas = Duvida.query.all()
    return render_template('duvidas.html', duvidas = duvidas)

@homeBlueprint.route('/duvida/add', methods = ["POST","GET"])
def addDuvida():
    if request.method == "GET":
        return render_template('addDuvida.html')
    if request.method == "POST":
        titulo = request.form.get('titulo')
        descricao = request.form.get('descricao')
        nome = request.form.get('nome_usuario')

        usuario = Usuario.query.filter_by(nome = nome).first()
        if not nome or not titulo:
           flash("Todos os campos devem ser preenchidos", 'error')
           return redirect(url_for("home.addDuvida"))

        duvida = Duvida(titulo = titulo, descricao = descricao, id_usuario = usuario.id)

        db.session.add(duvida)
        db.session.commit()

        return redirect(url_for('home.home'))