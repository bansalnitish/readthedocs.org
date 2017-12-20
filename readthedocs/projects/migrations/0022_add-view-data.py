# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-12-11 13:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0021_add-webhook-deprecation-feature'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domain',
            name='canonical',
            field=models.BooleanField(default=False, help_text='This Domain is the primary one where the documentation is served from'),
        ),
        migrations.AlterField(
            model_name='domain',
            name='count',
            field=models.IntegerField(default=0, help_text='Number of times this domain has been hit'),
        ),
        migrations.AlterField(
            model_name='project',
            name='allow_promos',
            field=models.BooleanField(default=True, help_text='If unchecked, users will still see community ads.', verbose_name='Allow paid advertising'),
        ),
        migrations.AlterField(
            model_name='project',
            name='comment_moderation',
            field=models.BooleanField(default=False, verbose_name='Comment Moderation'),
        ),
        migrations.AlterField(
            model_name='project',
            name='conf_py_file',
            field=models.CharField(blank=True, default=b'', help_text='Path from project root to <code>conf.py</code> file (ex. <code>docs/conf.py</code>). Leave blank if you want us to find it for you.', max_length=255, verbose_name='Python configuration file'),
        ),
        migrations.AlterField(
            model_name='project',
            name='has_valid_webhook',
            field=models.BooleanField(default=False, help_text='This project has been built with a webhook'),
        ),
        migrations.AlterField(
            model_name='project',
            name='programming_language',
            field=models.CharField(blank=True, choices=[('words', 'Only Words'), ('py', 'Python'), ('js', 'JavaScript'), ('php', 'PHP'), ('ruby', 'Ruby'), ('perl', 'Perl'), ('java', 'Java'), ('go', 'Go'), ('julia', 'Julia'), ('c', 'C'), ('csharp', 'C#'), ('cpp', 'C++'), ('objc', 'Objective-C'), ('other', 'Other')], default=b'words', help_text='The primary programming language the project is written in.', max_length=20, verbose_name='Programming Language'),
        ),
    ]