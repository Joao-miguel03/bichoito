from flask import Blueprint, render_template, redirect, request, url_for

homeBlueprint = Blueprint('home', __name__)

#rota inicial
@homeBlueprint.route('/', methods = ['GET'])
def home():
    return render_template('index.html')

@homeBlueprint.route('/sobrenos', methods = ['GET'])
def sobreNos():
    return render_template('sobreNos.html')