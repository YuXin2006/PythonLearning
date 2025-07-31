from django.db import models

# Create your models here.
class Question(models.Model):
    text=models.CharField(max_length=1000)
    pub_date=models.DateTimeField('date published')
    def __str__(self):
        return str(self.text)
class Choice(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    choice=models.TextField(max_length=200)
    votes=models.IntegerField(default=0)    
    def __str__(self):
        return f"{self.question.text}-->{self.choice}"