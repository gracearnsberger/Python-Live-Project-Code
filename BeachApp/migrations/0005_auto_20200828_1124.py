# Generated by Django 2.2.5 on 2020-08-28 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BeachApp', '0004_auto_20200824_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savecities',
            name='rate_city',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=1),
        ),
    ]
