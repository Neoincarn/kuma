# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-02-12 03:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0014_auto_20200110_0519"),
    ]

    operations = [
        migrations.RemoveField(model_name="user", name="tags",),
    ]