# Generated by Django 2.2.5 on 2020-08-21 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BeachApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savecities',
            name='rate_city',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=2),
        ),
    ]