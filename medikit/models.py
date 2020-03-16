from django.db import models


class Kit(models.Model):
    name = models.CharField(max_length=256)


class Drug(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    expiration_date = models.DateField()
    added = models.DateTimeField(auto_now_add=True)
    kit = models.ForeignKey(
        Kit,
        on_delete=models.CASCADE,
        related_name='drugs',
    )
