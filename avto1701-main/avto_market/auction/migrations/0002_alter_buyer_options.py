# Generated by Django 4.2.7 on 2024-01-03 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='buyer',
            options={'ordering': ['-last_bid_price']},
        ),
    ]
