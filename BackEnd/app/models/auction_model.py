from app import db

#Modulação da Tabela Lances
class Lance(db.Model):
    __tablename__ = 'lances'
    id_lance = db.Column(db.Integer, primary_key=True)
    valor_lance = db.Column(db.Float, nullable=False)
    data_lance = db.Column(db.Date, nullable=False)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'), nullable=False)
    id_produto = db.Column(db.Integer, db.ForeignKey('produtos.id_produto'), nullable=False)

    def to_dict(self):
        return {
            'id_lance': self.id_lance,
            'valor_lance': self.valor_lance,
            'data_lance': self.data_lance,
            'id_usuario': self.id_usuario,
            'id_produto': self.id_produto
        }
