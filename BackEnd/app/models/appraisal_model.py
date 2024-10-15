from app import db

#Modulação da tabela Avaliações
class Avaliacao(db.Model):
    __tablename__ = 'avaliacoes'
    id_avaliacao = db.Column(db.Integer, primary_key=True)
    texto = db.Column(db.Text, nullable=False)
    data = db.Column(db.Date, nullable=False)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'), nullable=False)
    id_produto = db.Column(db.Integer, db.ForeignKey('produtos.id_produto'), nullable=False)

    def to_dict(self):
        return {
            'id_avaliacao': self.id_avaliacao,
            'texto': self.texto,
            'data': self.data,
            'id_usuario': self.id_usuario,
            'id_produto': self.id_produto
        }
