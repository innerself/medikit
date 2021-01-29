# Generated by Django 3.1.5 on 2021-01-29 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medikit', '0003_kit_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('description', models.TextField()),
                ('expiration_date', models.DateField()),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('kit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medications', to='medikit.kit')),
            ],
        ),
        migrations.DeleteModel(
            name='Drug',
        ),
    ]
