from django.db import models
from myadmin.models import Datetime

# Create your models here.

class Student(models.Model):
    stdnum = models.IntegerField()
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    datetime = models.ForeignKey(Datetime, related_name="datetime_students", null=True, on_delete=models.SET_NULL, blank=True)
    topic = models.CharField(max_length=100)
    verification_code = models.CharField(max_length=50)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return str(self.stdnum) + ' - ' + self.email + ' - ' + self.datetime.__str__()