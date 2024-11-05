from mongoengine import Document, StringField, IntField, ListField, ReferenceField

# Modulação da Tabela Usuario
class Usuario(Document):
    id_usuario = IntField(required=True)
    nome = StringField(required=True)
    email = StringField(required=True)
    senha = StringField(required=True)
    reputacao = StringField(required=True)
    produtos = ListField(ReferenceField('Produto'))
    pagamentos = ListField(ReferenceField('Pagamento'))

    meta = {'collection': 'usuarios'}