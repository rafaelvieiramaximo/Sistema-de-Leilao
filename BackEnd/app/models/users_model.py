from mongoengine import Document, StringField, IntField, ListField, ReferenceField
import uuid

# Modulação da Tabela Usuario
class Usuario_Model(Document):
    nome = StringField(required=True)
    email = StringField(required=True)
    senha = StringField(required=True)
    reputacao = StringField(required=True)
    produtos = ListField(ReferenceField('Produto'))
    pagamentos = ListField(ReferenceField('Pagamento'))
    comunidade = ListField(ReferenceField('Comunidade'))   

    meta = {'collection': 'Usuarios'}