import datetime

from django.db import models


class Kit(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


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

    def __str__(self) -> str:
        return self.name

    @property
    def expired(self) -> bool:
        return (self.expiration_date - datetime.date.today()).days < 0

    @property
    def expires_in(self) -> datetime.timedelta:
        return self.expiration_date - datetime.date.today()
