#Aqui você define as "tabelas" do banco de dados usando a biblioteca SQLAlchemy.
from app import db

class Usuario(db.Model):
    id_usuario = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    senha = db.Column(db.String(255), nullable=False)
    reputacao = db.Column(db.Float, default=0)

    def to_dict(self):
        return {
            "id_usuario": self.id_usuario,
            "nome": self.nome,
            "email": self.email,
            "reputacao": self.reputacao
        }
