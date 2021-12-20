from django.db import models


# Create your models here.
class Technology(models.Model):
    id = models.CharField(max_length=5, primary_key=True)
    name = models.CharField(max_length=15)
    description = models.TextField()


class Person(models.Model):
    name = models.CharField(max_length=30)
    experience = models.IntegerField()
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE)
