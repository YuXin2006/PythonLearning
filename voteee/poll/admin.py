from django.contrib import admin
from poll.models import Question,Choice
# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)