from mongoengine import Document, StringField, FloatField, ObjectIdField

# Modulação da Tabela Usuario
class Usuario_Model(Document):
    nome = StringField(required=True)
    email = StringField(required=True)
    senha = StringField(required=True)
    reputacao = FloatField(required=True)

    meta = {'collection': 'Usuarios'}
