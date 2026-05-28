from django.db import models

class Task(models.Model):
    title = models.CharField()

class People(models.Model):
    name = models.CharField()

class Projects(models.Model):
    title = models.CharField('Project name', max_length=50)
    description = models.CharField('Opisanie')
    tasks = models.ManyToManyField(Task)
    peoples = models.ManyToManyField(People)
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.CharField()
