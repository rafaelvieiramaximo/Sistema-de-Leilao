from mongoengine import Document, StringField, IntField, ListField, ReferenceField
import uuid

# Modulação da Tabela Usuario
class Usuario_Model(Document):
    id_usuario = StringField(required=True, default=lambda: str(uuid.uuid4()), unique=True)
    nome = StringField(required=True)
    email = StringField(required=True)
    senha = StringField(required=True)
    reputacao = StringField(required=True)
    produtos = ListField(ReferenceField('Produto'))
    pagamentos = ListField(ReferenceField('Pagamento'))
    comunidade = ListField(ReferenceField('Comunidade'))   

    meta = {'collection': 'Usuarios'}