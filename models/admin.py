from mongoengine import *

class Admin(Document):
    email_address = StringField(required=True)
    password = BinaryField(required=True)
    admin_token = StringField(required=True)