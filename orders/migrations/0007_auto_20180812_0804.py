# Generated by Django 2.0.3 on 2018-08-12 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20180812_0804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='fulfilled',
            field=models.BooleanField(default=False),
        ),
    ]
