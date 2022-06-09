# Generated by Django 4.0.4 on 2022-06-07 16:22

from decimal import Decimal
from django.db import migrations
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='ordered_price',
            field=djmoney.models.fields.MoneyField(decimal_places=2, default=Decimal('0.0'), default_currency='MWK', max_digits=14),
        ),
    ]
