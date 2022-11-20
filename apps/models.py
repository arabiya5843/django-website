import datetime
from django.db import models
from django.db.models import Model


class User(Model):

    name = models.CharField(max_length=55)
    email = models.CharField(max_length=55)
    address = models.CharField(max_length=155)
    phone = models.CharField(max_length=55)
    age = models.DateField(default=1902)

    @property
    def get_age(self):
        return int((datetime.date.today() - self.age).days / 365)

    def __str__(self):
        return f'{self.name}'






