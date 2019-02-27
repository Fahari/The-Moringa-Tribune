# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-27 07:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_editor_article_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='editor',
            name='article_image',
        ),
        migrations.AddField(
            model_name='article',
            name='article_image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='articles/'),
            preserve_default=False,
        ),
    ]
