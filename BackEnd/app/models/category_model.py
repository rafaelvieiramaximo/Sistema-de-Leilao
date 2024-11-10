from mongoengine import Document, StringField, FloatField, IntField, DateField, ReferenceField

class Categoria_Model(Document):
    id_categoria = IntField(primary_key=True, required=True)
    nome = StringField(max_length=255, required=True)