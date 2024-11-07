from mongoengine import Document, StringField, IntField, ReferenceField

#Modulação da Tabela Comunidade
class Comunidade(Document):
    id_comunidade = IntField(primary_key=True, required=True)
    nome = StringField(max_length=255, required=True)
    usuario = ReferenceField('Usuario', required=True)

    meta = {'collection': 'comunidade'}
