# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-20 07:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djpaypal', '0002_billingagreement_end_of_period'),
    ]

    operations = [
        migrations.AddField(
            model_name='webhookeventtrigger',
            name='remote_ip',
            field=models.GenericIPAddressField(default='0.0.0.0', help_text='IP address of the request client.'),
            preserve_default=False,
        ),
    ]
