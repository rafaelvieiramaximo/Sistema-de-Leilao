from app import db

#Modulação da Tabela Comunidade
class Comunidade(db.Model):
    __tablename__ = 'comunidade'
    id_comunidade = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'), nullable=False)

    def to_dict(self):
        return {
            'id_comunidade': self.id_comunidade,
            'nome': self.nome,
            'id_usuario': self.id_usuario
        }
