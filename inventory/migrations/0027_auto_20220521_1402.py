# Generated by Django 3.2 on 2022-05-21 14:02

from decimal import Decimal
from django.db import migrations
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0026_auto_20220521_1334'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='total_cost_price',
            field=djmoney.models.fields.MoneyField(decimal_places=2, default=Decimal('0'), default_currency='MWK', max_digits=14),
        ),
        migrations.AddField(
            model_name='item',
            name='total_cost_price_currency',
            field=djmoney.models.fields.CurrencyField(choices=[('MWK', 'Malawian Kwacha')], default='MWK', editable=False, max_length=3),
        ),
    ]
