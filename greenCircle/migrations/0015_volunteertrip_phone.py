# Generated by Django 3.0 on 2022-01-26 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('greenCircle', '0014_volunteertrip_accept_pay'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteertrip',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
