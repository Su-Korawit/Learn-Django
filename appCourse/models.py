from django.db import models

class teachers(models.Model):
    firstname = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)
    majorGroup = models.CharField(max_length=30)
    subjectSet = models.ManyToManyField('appCourse.subjects')

class subjects(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=60)
    grade = models.IntegerField()