from mongoengine import *
import datetime

class User(Document):
    email_address = StringField(required=True)
    password = BinaryField(required=True)
    name = StringField(required=True)
    client_type = StringField(required=True)
    education_level = StringField(required=True)
    specialization = StringField(required=True)
    account_balance = DecimalField(default='0.00')
    age = IntField(required=True)
    gender = StringField(required=True)
    date_created = DateTimeField(default=datetime.datetime.utcnow)
    dg_token = StringField(required=True)