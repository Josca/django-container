from django.db import models


class Sample(models.Model):
    timestamp = models.DateTimeField(null=False, primary_key=True)
    value = models.FloatField(default=0.0)
