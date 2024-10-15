from app import db

#Modulção da Tabela Frete
class Frete(db.Model):
    __tablename__ = 'frete'
    cte = db.Column(db.Integer, primary_key=True)
    tipo_frete = db.Column(db.String(255), nullable=False)
    valor_frete = db.Column(db.Float)
    prazo_entrega = db.Column(db.Integer)
    id_pagamento = db.Column(db.Integer, db.ForeignKey('pagamentos.id_pagamento'))

    def to_dict(self):
        return {
            'cte': self.cte,
            'tipo_frete': self.tipo_frete,
            'valor_frete': self.valor_frete,
            'prazo_entrega': self.prazo_entrega,
            'id_pagamento': self.id_pagamento
        }
