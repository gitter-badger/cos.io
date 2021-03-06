# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-17 18:49
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_merge_20161017_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='content',
            field=wagtail.wagtailcore.
            fields.StreamField(
                (
                    ('rich_text', wagtail.wagtailcore.blocks.RichTextBlock()),
                    ('code_block', wagtail.wagtailcore.blocks.StructBlock(
                        (('language', wagtail.wagtailcore.blocks.ChoiceBlock(
                            choices=[
                                ('python', 'python'),
                                ('css', 'css'),
                                ('sql', 'sql'),
                                ('javascript', 'javascript'),
                                ('clike', 'clike'),
                                ('markup', 'markup'),
                                ('java', 'java')],
                            default='python')),
                         ('codes', wagtail.wagtailcore.blocks.TextBlock())))),
                    ('google_calendar',
                     wagtail.wagtailcore.blocks.StructBlock(
                         (
                             ('source', wagtail.wagtailcore.blocks.CharBlock(
                                 help_text='Such as: calendar@cos.io',
                                 max_length=255,
                                 required=True)),)))),
                blank=True,
                null=True),
        ),
    ]
