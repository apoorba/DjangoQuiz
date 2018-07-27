from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import CASCADE


class Question(models.Model):
    question_text = models.CharField(max_length=100)
    option1 = models.CharField(max_length=50)
    option2 = models.CharField(max_length=50)
    option3 = models.CharField(max_length=50)
    option4 = models.CharField(max_length=50)
    correct_answer = models.CharField(max_length=50)
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.question_text


class Score(models.Model):
    question = models.ForeignKey(Question, on_delete=CASCADE)
    score = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=CASCADE, null=True)
