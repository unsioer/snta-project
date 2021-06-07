from django.db import models

# Create your models here.
class Weibo(models.Model):
    author = models.CharField(max_length=256)
    main_page = models.CharField(max_length=256)
    content = models.CharField(max_length=512)
    location = models.CharField(max_length=256,null=True)
    time = models.CharField(max_length=256)
    url = models.CharField(max_length=256)
    source = models.CharField(max_length=256,null=True)
    share = models.IntegerField()
    comment = models.IntegerField()
    like = models.IntegerField()
    label = models.CharField(max_length=256)
    def __str__(self):
        return self.content

class LabelWord(models.Model):
    word = models.CharField(max_length=256)
    weight = models.FloatField()
    label = models.CharField(max_length=256)
    def __str__(self):
        return self.word

class ClusterWord(models.Model):
    word = models.CharField(max_length=256)
    weight = models.FloatField()
    cluster = models.IntegerField()
    def __str__(self):
        return self.word

class MonthSentiment(models.Model):
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
        return self.date