from django.db import models

from model_utils.models import TimeStampedModel


class Exam(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=250)


class Pupil(TimeStampedModel):
    first_name = models.TextField(max_length=50)
    last_name = models.TextField(max_length=50)
    email_address = models.TextField(max_length=100)


class Teacher(TimeStampedModel):

    def __str__(self):
        return self.username

    username = models.TextField(max_length=50)
    password = models.TextField(max_length=20)


class ExamQuestions(models.Model):

    def __str__(self):
        return self.question

    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    question = models.CharField(max_length=200)
    multiple_choice = models.BooleanField(default=False)
    multi_choice1 = models.CharField(max_length=200, blank=True, null=True)
    multi_choice2 = models.CharField(max_length=200, blank=True, null=True)
    multi_choice3 = models.CharField(max_length=200, blank=True, null=True)
    correct_answer = models.CharField(max_length=200)
    score = models.FloatField()


class ExamResults(models.Model):
    user = models.ForeignKey(Pupil, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    result = models.FloatField()
