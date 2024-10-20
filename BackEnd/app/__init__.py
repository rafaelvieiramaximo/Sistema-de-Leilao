#Aqui você inicia o Flask e define configurações básicas, como o banco de dados.
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_cors import CORS  # Importa o CORS   
import os



load_dotenv()  # Carrega variáveis de ambiente do.env


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)


    #Troca a url do BD pela variavel DB_KEY se utilizando as bibliotecas os e env.
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_KEY')  # Caminho do banco de dados

    db.init_app(app)

    CORS(app)  # Permite CORS para todas as rotas e origens
    
    # Cria todas as tabelas, respeitando a ordem de dependências
    with app.app_context():
        db.create_all()

    from .routes import routes as routes_bp
    app.register_blueprint(routes_bp)  # Registra as rotas definidas no arquivo routes.py

    return app
