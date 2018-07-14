from mongoengine import *
from user import User
from stages import Stages
import datetime

class Booking(Document):
    user_id = ReferenceField(User)
    stage_in_process = EmbeddedDocumentField(Stages)
    notes = StringField(default='')
    date_created = DateTimeField(default=datetime.datetime.utcnow)
    services_required = ListField(StringField)
    balance = DecimalField(default='0.00')
    deadline = StringField(required=True)
