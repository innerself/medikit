from django.db import models


class Drug(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    expiration_date = models.DateField()
    added = models.DateTimeField(auto_now_add=True)
