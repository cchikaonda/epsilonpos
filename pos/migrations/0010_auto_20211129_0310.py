# Generated by Django 3.0.9 on 2021-11-29 03:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0009_customer_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='laybyorders',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 11, 29, 3, 10, 22, 881212)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='laybyorders',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='vat_p',
            field=models.FloatField(default=0.0),
        ),
    ]
