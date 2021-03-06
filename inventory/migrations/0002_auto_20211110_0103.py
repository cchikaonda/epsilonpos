# Generated by Django 3.0.9 on 2021-11-10 01:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='created_at',
            field=models.DateField(auto_created=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stock',
            name='new_quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='stock',
            name='previous_quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='stock',
            name='stock_in',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='stock',
            name='unit_quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='stock',
            name='updated_at',
            field=models.DateField(auto_created=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
