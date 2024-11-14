from mongoengine import Document, StringField, IntField, ReferenceField, DateField, DateTimeField
#Modulação da tabela Avaliações
class Avaliacao_Model(Document):
    texto = StringField(required=True)
    data = DateField(required=True)
    usuario = ReferenceField('Usuario', required=True)
    produto = ReferenceField('Produto', required=True)

    meta = {'collection': 'avaliacoes'}
    
