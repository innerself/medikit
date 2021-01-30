import datetime

from django.conf import settings
from django.db import models
from pytils.translit import slugify


class Kit(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='kits',
    )

    class Meta:
        unique_together = ['name', 'user']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Medication(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    description = models.TextField(blank=True)
    expiration_date = models.DateField(blank=True, null=True)
    added = models.DateTimeField(auto_now_add=True)
    kit = models.ForeignKey(
        Kit,
        on_delete=models.CASCADE,
        related_name='medications',
    )

    def __str__(self) -> str:
        return self.name

    @property
    def expired(self) -> bool:
        return (self.expiration_date - datetime.date.today()).days < 0

    @property
    def expires_in(self) -> datetime.timedelta:
        return self.expiration_date - datetime.date.today()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
