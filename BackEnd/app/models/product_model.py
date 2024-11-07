from mongoengine import Document, StringField, FloatField, IntField, DateField, ReferenceField

#Modulação da Tabela do Produto
class Produto(Document):
    id_produto = IntField(primary_key=True, required=True)
    nome = StringField(max_length=255, required=True)
    descricao = StringField()
    preco_inicial = FloatField(required=True)
    data_inicial = DateField(required=True)
    usuario = ReferenceField('Usuario', required=True)

    meta = {'collections': 'produtos'}