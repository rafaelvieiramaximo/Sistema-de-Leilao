#Aqui você define as "tabelas" do banco de dados usando a biblioteca SQLAlchemy.
from __init__ import db
from mongoengine import Document, StringField, FloatField, IntField, ListField, ReferenceField
from models import Produto

#Modulação da Tabela Usuario
class Usuario(db.Document):
    id_usuario = db.IntField(required=True)
    nome = db.StringField(required=True)
    email = db.StringField(required=True)
    senha = db.StringField(required=True)
    reputacao = db.StringField(required=True)
    produtos = ListField(ReferenceField(Produto))

    meta = {'collection': 'usuarios'}
