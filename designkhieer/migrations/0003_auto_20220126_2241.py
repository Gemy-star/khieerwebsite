# Generated by Django 3.0 on 2022-01-26 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designkhieer', '0002_alter_khieerdesign_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='khieerdesign',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
