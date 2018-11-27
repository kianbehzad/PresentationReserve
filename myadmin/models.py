from django.db import models

# Create your models here.

class Datetime(models.Model):
    date = models.CharField(max_length=15)
    num_stars = models.IntegerField()

    def __str__(self):
        return self.date + '  ' + self.num_stars + 'X*'