# Generated by Django 3.0 on 2022-02-28 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('greenCircle', '0017_auto_20220126_2328'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='volunteertrip',
            name='accept_pay',
        ),
    ]
