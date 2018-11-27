from django.db import models

# Create your models here.

class Datetime(models.Model):
    year = models.IntegerField()
    month = models.IntegerField()
    day = models.IntegerField()
    number_of_stars = models.IntegerField(default=0)

    def __str__(self):
        return str(self.year) + '/' + str(self.month) + '/' + str(self.day) + '   :  ' + str(self.number_of_stars) + '+'