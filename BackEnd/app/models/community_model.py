from mongoengine import Document, StringField, IntField, ReferenceField
from app.models.users_model import Usuario_Model

#Modulação da Tabela Comunidade
class Comunidade_Model(Document):
    nome = StringField(max_length=255, required=True)
    id_usuario = ReferenceField(Usuario_Model, required=True)

    meta = {'collection': 'comunidade'}
