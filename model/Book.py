# from mongoengine import Document
# from mongoengine.fields import StringField, ReferenceField, IntField, ListField, ObjectIdField

# class Book(Document):
#     _id = ObjectIdField()
#     name = StringField(required = True)
#     author = StringField(required = True)
#     type = StringField(required = True)
#     numberPage = IntField(required = True)
#     imgDes = StringField(required = True)
#     description = StringField(required = True)
#     publisher = StringField(required = True)
#     tableOfContent = ListField()
#     comments = ListField(ReferenceField('comment'))