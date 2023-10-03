from django.db import models

class AnomalyData(models.Model):
    return_temp = models.FloatField()
    outdoor_temp = models.FloatField()
    relative_humidity = models.FloatField()
    is_anomaly = models.BooleanField(null=True)  
