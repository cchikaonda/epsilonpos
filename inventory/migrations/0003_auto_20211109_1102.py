# Generated by Django 3.0.9 on 2021-11-09 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20211107_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='previous_quantity',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='stock_in',
            field=models.IntegerField(),
        ),
    ]
