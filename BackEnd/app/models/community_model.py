from mongoengine import Document, StringField, IntField, ReferenceField
from app.models.users_model import Usuario_Model

#Modulação da Tabela Comunidade
class Comunidade_Model(Document):
    nome = StringField(required=True)
    
    meta = {'collection': 'Comunidade'}
