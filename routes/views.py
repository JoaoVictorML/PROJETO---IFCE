from flask import Blueprint, render_template, request, redirect, url_for
from extensions import db      # IMPORTANTE: de extensions!
from models.users import Users # Certifique-se que está Users (com S)ç               # Importando a instância do banco

# Criando o Blueprint
views_bp = Blueprint('views', __name__)

@views_bp.route('/')
def index():
    return render_template('index.html')

@views_bp.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# MUDANÇA AQUI: Use @views_bp em vez de @app
@views_bp.route('/register', methods=['POST'])
def register_user():
    nome = request.form.get('nome')
    email = request.form.get('email')
    senha = request.form.get('senha')

    # Cria o objeto e salva no banco
    new_user = Users(nome=nome, email=email, senha=senha)
    db.session.add(new_user)
    db.session.commit()

    # Redireciona para a página inicial do blueprint
    return redirect(url_for('views.index'))