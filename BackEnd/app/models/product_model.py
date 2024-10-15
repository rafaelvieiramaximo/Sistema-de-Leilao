from app import db


#Modulação da Tabela do Produto
class Produto(db.Model):
    __tablename__ = 'produtos'
    id_produto = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    descricao = db.Column(db.Text)
    preco_inicial = db.Column(db.Float, nullable=False)
    data_inicial = db.Column(db.Date, nullable=False)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'), nullable=False)

    def to_dict(self):
        return {
            'id_produto': self.id_produto,
            'nome': self.nome,
            'descricao': self.descricao,
            'preco_inicial': self.preco_inicial,
            'data_inicial': self.data_inicial,
            'id_usuario': self.id_usuario
        }
