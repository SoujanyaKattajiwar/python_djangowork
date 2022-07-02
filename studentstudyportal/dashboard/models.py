from django.db import models
from django.contrib.auth.models import User


class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'notes'
        verbose_name = 'notes'
        verbose_name_plural = 'notes'

class Homework(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    subject=models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    description = models.TextField()
    due=models.DateTimeField()
    is_finished=models.BooleanField(default=False)

    def __str__(self):
        return self.subject

    class Meta:
        db_table='homework'
        verbose_name='homework'
        verbose_name_plural='homework'

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    is_finished = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        db_table='todo'

