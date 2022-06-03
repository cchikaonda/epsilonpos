# Generated by Django 4.0.4 on 2022-06-03 13:50

from decimal import Decimal
from django.db import migrations
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0040_remove_payment_service_fee_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='service_fee',
            field=djmoney.models.fields.MoneyField(decimal_places=2, default=Decimal('0.0'), default_currency='MWK', max_digits=14),
        ),
        migrations.AddField(
            model_name='payment',
            name='service_fee_currency',
            field=djmoney.models.fields.CurrencyField(choices=[('MWK', 'Malawian Kwacha')], default='MWK', editable=False, max_length=3),
        ),
    ]
