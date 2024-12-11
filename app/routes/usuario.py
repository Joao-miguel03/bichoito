from flask import Blueprint, render_template, redirect, request, url_for, flash, Response
from app.models.usuario import Usuario
from app.__init__ import db

usuarioBlueprint = Blueprint('usuario', __name__, url_prefix='/usuario')

@usuarioBlueprint.route('/cadastro', methods = ['GET', 'POST'])
def cadastro():
    if request.method == 'GET':
        return render_template('adicionarUsuario.html')
    elif request.method == 'POST': 
    
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')
        if not nome or not email or not senha:
            flash("Todos os campos devem ser preenchidos", 'error')
            return redirect(url_for("usuario.cadastro"))
        
        novo_usuario = Usuario(nome = nome, email = email, senha = senha)

        db.session.add(novo_usuario)
        db.session.commit()
        print("Funcionou!")
         
        return redirect(url_for('home.home'))
    
@usuarioBlueprint.route("/update/<int:usuario_id>", methods = ['GET','POST'])
def update(usuario_id):
    if request.method == 'GET':
        usuario = Usuario.query.filter_by(id=usuario_id).first()
        return render_template("updateUser.html", usuario = usuario)
    if request.method == 'POST':
        usuario = Usuario.query.filter_by(id = usuario_id).first()

        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')
        foto_perfil = request.files['foto_perfil']

        if not nome or not email:
            flash('Todos os campos devem ser preenchidos!', 'error')
            return redirect(url_for('home.home'))
        
        try:
            usuario.nome = nome
            usuario.email = email
            usuario.senha = senha
            usuario.foto_perfil = foto_perfil.read()
        except:
            usuario.nome = nome
            usuario.email = email
            usuario.senha = senha

        db.session.commit()

        print("Funcionou!")
        return redirect(url_for('adm.listar'))

@usuarioBlueprint.route('/foto/<int:usuario_id>', methods = ['GET'])
def foto(usuario_id):
    usuario = Usuario.query.get_or_404(usuario_id)
    if usuario.foto_perfil:
        return Response(usuario.foto_perfil, mimetype='image/jpeg')
    else:
        # Retornar uma imagem padrão caso não tenha foto
        return redirect(url_for('static', filename='default.png'))



