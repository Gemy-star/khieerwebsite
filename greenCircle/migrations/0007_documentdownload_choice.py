# Generated by Django 3.0 on 2022-01-10 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('greenCircle', '0006_documentdownload'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentdownload',
            name='choice',
            field=models.CharField(blank=True, choices=[('1_TATOF', 'دليل التعاطف'), ('2_GREEN', 'تكوين دائرة')], max_length=255, null=True),
        ),
    ]
