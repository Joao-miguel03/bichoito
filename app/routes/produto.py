from flask import Blueprint, render_template, redirect, url_for, Response, request, flash
from app.models.petiscoCachorro import PetiscoCachorro
from app.models.petiscoGato import PetiscoGato
from app.models.brinquedo import Brinquedo
from app.__init__ import db

produtoBlueprint = Blueprint('produto', __name__, url_prefix="/produto")

@produtoBlueprint.route('/', methods = ['GET'])
def home():
    return render_template('tiposProdutos.html')

@produtoBlueprint.route('/add', methods = ['GET','POST'])
def add():
    if request.method == "GET":
        return render_template('addProduto.html')
    elif request.method == 'POST':
        tipo = request.form.get('tipo')
        nome = request.form.get('nome')
        descricao = request.form.get('descricao')
        preco = request.form.get('preco')
        disponivel = request.form.get('disponivel')
        imagem = request.files['imagem']

        if disponivel == "sim":
            disponivel = True
        elif disponivel == "nao":
            disponivel = False

        try:
            float(preco)
        except:
            return ("valor invalido", 400)

        if not nome or not descricao or not preco or not disponivel:
            flash('Todos os campos devem ser preenchidos!', 'error')
            return redirect(url_for('produto.add'))
        
        match tipo:
            case 'brinquedo':
                novo_produto = Brinquedo(nome = nome, descricao = descricao, preco = preco, disponivel = disponivel, imagem = imagem.read())
            case 'petiscoC':
                novo_produto = PetiscoCachorro(nome = nome, descricao = descricao, preco = preco, disponivel = disponivel, imagem = imagem.read())
            case 'petiscoG':
                novo_produto = PetiscoGato(nome = nome, descricao = descricao, preco = preco, disponivel = disponivel, imagem = imagem.read())

        db.session.add(novo_produto)
        db.session.commit()

        print("Funcionou!")

        return redirect(url_for('adm.listar_tudo'))
    
@produtoBlueprint.route('/update/<int:produto_id>', methods = ["GET", "POST"])
def update(produto_id):
    if request.method == "GET":
        return render_template('updateProduto.html') 
    if request.method == "POST":
        try:
            produto = PetiscoCachorro.query.filter_by(id = produto_id).first()
        except:
            try:
                produto = PetiscoGato.query.filter_by(id= produto_id).first()
            except:
                produto = Brinquedo.query.filter_by(id = produto_id).first()
        
        produto
        


@produtoBlueprint.route('/foto/<int:produto_id>', methods = ['GET'])
def foto(produto_id):
    try:
        produto = PetiscoGato.query.get_or_404(produto_id)
    except:
        try:
            produto = PetiscoCachorro.query.get_or_404(produto_id)
        except:    
            produto = Brinquedo.query.get_or_404(produto_id)
            

    if produto.imagem:
        return Response(produto.imagem, mimetype='image/jpeg')
    else:
        # Retornar uma imagem padrão caso não tenha foto
        return redirect(url_for('static', filename='default.png'))
