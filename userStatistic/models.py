from django.db import models
from django.utils import timezone

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Statistic(models.Model):
    dateTime = models.DateTimeField()
    tonicAvg = models.IntegerField()
    peaksCount = models.IntegerField()
    user_id = models.ForeignKey(User, related_name='statistic', on_delete=models.CASCADE)

    def __str__(self):
        return self.user_id.name+' '+str(self.date)
