from mongoengine import Document, FloatField, DateField, IntField, ReferenceField
#Modulação da Tabela Lances
class Lance_Model(Document):
    valor_lance = FloatField(required=True)
    data_lance = DateField(required=True)
    usuario = ReferenceField('Usuario', required=True)
    produto = ReferenceField('Produto', required=True)

    meta = {'collection': 'Lances'}