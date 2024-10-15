from app import db

#Modulação da Tabela Pagamentos
class Pagamento(db.Model):
    __tablename__ = 'pagamentos'
    id_pagamento = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'), nullable=False)
    id_produto = db.Column(db.Integer, db.ForeignKey('produtos.id_produto'), nullable=False)
    valor_total = db.Column(db.Float, nullable=False)
    forma_pagamento = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(255), nullable=False)

    def to_dict(self):
        return {
            'id_pagamento': self.id_pagamento,
            'id_usuario': self.id_usuario,
            'id_produto': self.id_produto,
            'valor_total': self.valor_total,
            'forma_pagamento': self.forma_pagamento,
            'status': self.status
        }
