from mongoengine import *

class Stages(EmbeddedDocument):
    one = BooleanField(default=True)
    two = BooleanField(default=False)
    three = BooleanField(default=False)
    four = BooleanField(default=False)
    five = BooleanField(default=False)
