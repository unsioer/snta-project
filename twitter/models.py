from django.db import models

# Create your models here.
class Tweet(models.Model):
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=256)
    date = models.CharField(max_length=256)
    created_time = models.CharField(max_length=256)
    content = models.CharField(max_length=512)
    share = models.IntegerField()
    comment = models.IntegerField()
    like = models.IntegerField()
    label = models.CharField(max_length=256)
    def __str__(self):
        return self.content


'''class MonthSentiment(models.Model):
    month = models.CharField(max_length=256)
    neutralBiden = models.FloatField()
    neutralTrump = models.FloatField()
    positiveBiden = models.FloatField()
    positiveTrump = models.FloatField()
    negativeBiden = models.FloatField()
    negativeTrump = models.FloatField()
    def __str__(self):
        return self.month

class DaySentiment(models.Model):
    date = models.CharField(max_length=256)
    neutralBiden = models.FloatField()
    neutralTrump = models.FloatField()
    positiveBiden = models.FloatField()
    positiveTrump = models.FloatField()
    negativeBiden = models.FloatField()
    negativeTrump = models.FloatField()
    def __str__(self):
        return self.date'''