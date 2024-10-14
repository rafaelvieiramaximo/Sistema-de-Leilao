#Define as "rotas", ou seja, os URLs que sua aplicação vai expor para o usuário, 
# como /produtos, /usuarios, etc.
from app import app

@app.route('/')
@app.route('/index')
def index():
    return 'Hello, World!'