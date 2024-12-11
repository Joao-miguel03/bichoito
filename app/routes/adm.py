from flask import Blueprint, render_template, redirect, request, url_for
from app.models.usuario import Usuario
from app.models.petiscoCachorro import PetiscoCachorro
from app.models.petiscoGato import PetiscoGato
from app.models.brinquedo import Brinquedo
from app.__init__ import db

admBlueprint = Blueprint("adm", __name__, url_prefix="/adm")

@admBlueprint.route("/")
def home():
    return render_template("rotaADM.html")

@admBlueprint.route('/listar', methods = ['GET'])
def listar():
    usuarios = Usuario.query.all()
    produtosCachorro = PetiscoCachorro.query.all()
    produtosGato = PetiscoGato.query.all()
    produtosBrinquedo = Brinquedo.query.all()

    return render_template("listarTudo.html", usuarios = usuarios, produtosCachorro = produtosCachorro, produtosGato = produtosGato, produtosBrinquedo = produtosBrinquedo)