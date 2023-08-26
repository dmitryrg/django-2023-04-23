from django.db import models

class Sensor(models.Model):
    name = models.CharField(max_length=70)
    description = models.CharField(max_length=256)

    class Meta:
        ordering = ['name']


class Measurement(models.Model):
    temperature = models.DecimalField(decimal_places=1, max_digits=4)
    created_at = models.DateTimeField(auto_now=True)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
