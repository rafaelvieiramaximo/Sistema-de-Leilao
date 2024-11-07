from flask import Flask
from flask_mongoengine import MongoEngine
from dotenv import load_dotenv
from flask_cors import CORS
from app.routes import routes
from app.db import db

import os

load_dotenv()  # Carrega variáveis de ambiente do arquivo .env


def create_app():
    app = Flask(__name__)

    # Configuração do MongoDB usando MongoEngine
    app.config['MONGODB_SETTINGS'] = {
        'host': os.getenv('DB_KEY') 
    }

    db.init_app(app)

    CORS(app)  # Permite CORS para todas as rotas e origens

    # Registro das rotas do aplicativo
    app.register_blueprint(routes)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)