# Generated by Django 3.1.1 on 2020-09-19 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0002_auto_20200918_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
