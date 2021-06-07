from django.db import models
import json

# Create your models here.
class HubeiCityCases(models.Model):
    cityName=models.CharField(max_length=256)
    confirmCount=models.IntegerField()
    suspectedCount=models.IntegerField()
    curedCount=models.IntegerField()
    deadCount=models.IntegerField()
    updateTime=models.TimeField()
    year=models.IntegerField()
    month=models.IntegerField()
    day=models.IntegerField()
    def __str__(self):
        return json.dumps({'confirmCount':self.confirmCount, 
                            'cityName':self.cityName,
                            'year':self.year,
                            'month':self.month,
                            'day':self.day,
                            })

class HubeiProvinceCases(models.Model):
    confirmCount=models.IntegerField()
    suspectedCount=models.IntegerField()
    curedCount=models.IntegerField()
    deadCount=models.IntegerField()
    updateTime=models.TimeField()
    year=models.IntegerField()
    month=models.IntegerField()
    day=models.IntegerField()
    def __str__(self):
        return json.dumps({'confirmCount':self.confirmCount,
                            'year':self.year,
                            'month':self.month,
                            'day':self.day,
                            })