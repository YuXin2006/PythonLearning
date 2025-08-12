from django.db.models import *


class Course(Model):
    id=IntegerField(primary_key=True)
    name=CharField(max_length=100)
    code=CharField(max_length=100)
    description=CharField(max_length=1000)