# Generated by Django 2.0.7 on 2018-07-17 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zayacab', '0012_auto_20180717_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='fare',
            field=models.FloatField(null=True),
        ),
    ]
