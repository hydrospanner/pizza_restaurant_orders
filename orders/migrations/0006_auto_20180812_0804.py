# Generated by Django 2.0.3 on 2018-08-12 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_order_placed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='pending',
            new_name='fulfilled',
        ),
    ]
