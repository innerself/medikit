# Generated by Django 3.1.6 on 2021-02-02 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medikit', '0007_auto_20210202_1919'),
    ]

    operations = [
        migrations.AddField(
            model_name='kit',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
