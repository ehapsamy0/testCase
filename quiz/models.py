# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.


User = get_user_model()
class Quiz(models.Model):
    name = models.CharField(max_length=200)



    def __str__(self):
        return f'{self.name}'



class TypeQuestion(models.Model):
    name = models.CharField(max_length=120)


    def __str__(self):
        return f'{self.name}'



class Question(models.Model):
    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    type_question = models.ForeignKey(TypeQuestion,on_delete=models.CASCADE,default=1)

    def __str__(self):
       return f'{self.title}'


class Answer(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    answer_cho = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.answer_cho}'


class UserAnswers(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    answer_text = models.PositiveIntegerField()
    submited = models.BooleanField(default=False)


    def __str__(self):
        return f'{self.quiz}'
