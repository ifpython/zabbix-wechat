# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 10:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zabbix_wechat_db', '0002_duty_roster_token'),
    ]

    operations = [
        migrations.CreateModel(
            name='GROUP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GROUPNAME', models.CharField(max_length=32)),
                ('PARTY', models.CharField(max_length=64)),
            ],
        ),
    ]