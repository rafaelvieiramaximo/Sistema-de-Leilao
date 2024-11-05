from flask import Flask
from flask_mongoengine import MongoEngine
from dotenv import load_dotenv
from flask_cors import CORS
import os

load_dotenv()  # Carrega variáveis de ambiente do arquivo .env

db = MongoEngine()

def create_app():
    app = Flask(__name__)

    # Configuração do MongoDB usando MongoEngine
    app.config['MONGODB_SETTINGS'] = {
        'db': os.getenv('DB_NAME'),        # Nome do banco de dados
        'host': os.getenv('DB_HOST'),      # Endereço do servidor MongoDB
        'port': int(os.getenv('DB_PORT')), # Porta do MongoDB
        'username': os.getenv('DB_USER'),  # Usuário do banco, se aplicável
        'password': os.getenv('DB_PASS'),  # Senha do banco, se aplicável
        'authentication_source': 'admin'   # Fonte de autenticação, se necessária
    }

    db.init_app(app)

    CORS(app)  # Permite CORS para todas as rotas e origens

    # Registro das rotas do aplicativo
    from .routes import routes as routes_bp
    app.register_blueprint(routes_bp)

    return app
