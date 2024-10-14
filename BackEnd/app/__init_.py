#Aqui você inicia o Flask e define configurações básicas, como o banco de dados.
from flask import Flask
app = Flask(__name__)

from app import routes

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
