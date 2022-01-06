# Generated by Django 3.0 on 2022-01-05 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('greenCircle', '0005_auto_20210912_2053'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentDownload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('destination', models.SmallIntegerField(choices=[(1, 'افراد'), (2, 'قطاع عام'), (3, 'قطاع خاص'), (4, 'قطاع غير ربحى')], null=True)),
            ],
        ),
    ]