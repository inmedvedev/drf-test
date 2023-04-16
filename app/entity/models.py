from django.db import models
from django.contrib.auth.models import User


class Entity(models.Model):
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.IntegerField("Value", default=0)
    properties = models.ManyToManyField("Property")


class Property(models.Model):
    key = models.CharField("Key", max_length=100, blank=True)
    value = models.CharField("Value", max_length=100, blank=True)
