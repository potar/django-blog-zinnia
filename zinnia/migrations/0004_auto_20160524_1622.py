# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zinnia', '0003_publication_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description_en',
            field=models.TextField(null=True, verbose_name='description', blank=True),
        ),
        migrations.AddField(
            model_name='category',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='description', blank=True),
        ),
        migrations.AddField(
            model_name='category',
            name='description_uk',
            field=models.TextField(null=True, verbose_name='description', blank=True),
        ),
        migrations.AddField(
            model_name='category',
            name='slug_en',
            field=models.SlugField(null=True, max_length=255, help_text="Used to build the category's URL.", unique=True, verbose_name='slug'),
        ),
        migrations.AddField(
            model_name='category',
            name='slug_ru',
            field=models.SlugField(null=True, max_length=255, help_text="Used to build the category's URL.", unique=True, verbose_name='slug'),
        ),
        migrations.AddField(
            model_name='category',
            name='slug_uk',
            field=models.SlugField(null=True, max_length=255, help_text="Used to build the category's URL.", unique=True, verbose_name='slug'),
        ),
        migrations.AddField(
            model_name='category',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='category',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='category',
            name='title_uk',
            field=models.CharField(max_length=255, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='entry',
            name='content_en',
            field=models.TextField(null=True, verbose_name='content', blank=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='content_ru',
            field=models.TextField(null=True, verbose_name='content', blank=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='content_uk',
            field=models.TextField(null=True, verbose_name='content', blank=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='excerpt_en',
            field=models.TextField(help_text='Used for SEO purposes.', null=True, verbose_name='excerpt', blank=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='excerpt_ru',
            field=models.TextField(help_text='Used for SEO purposes.', null=True, verbose_name='excerpt', blank=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='excerpt_uk',
            field=models.TextField(help_text='Used for SEO purposes.', null=True, verbose_name='excerpt', blank=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='image_caption_en',
            field=models.TextField(help_text="Image's caption.", null=True, verbose_name='caption', blank=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='image_caption_ru',
            field=models.TextField(help_text="Image's caption.", null=True, verbose_name='caption', blank=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='image_caption_uk',
            field=models.TextField(help_text="Image's caption.", null=True, verbose_name='caption', blank=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='lead_en',
            field=models.TextField(help_text='Lead paragraph', null=True, verbose_name='lead', blank=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='lead_ru',
            field=models.TextField(help_text='Lead paragraph', null=True, verbose_name='lead', blank=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='lead_uk',
            field=models.TextField(help_text='Lead paragraph', null=True, verbose_name='lead', blank=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='slug_en',
            field=models.SlugField(unique_for_date=b'publication_date', max_length=255, help_text="Used to build the entry's URL.", null=True, verbose_name='slug'),
        ),
        migrations.AddField(
            model_name='entry',
            name='slug_ru',
            field=models.SlugField(unique_for_date=b'publication_date', max_length=255, help_text="Used to build the entry's URL.", null=True, verbose_name='slug'),
        ),
        migrations.AddField(
            model_name='entry',
            name='slug_uk',
            field=models.SlugField(unique_for_date=b'publication_date', max_length=255, help_text="Used to build the entry's URL.", null=True, verbose_name='slug'),
        ),
        migrations.AddField(
            model_name='entry',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='entry',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='entry',
            name='title_uk',
            field=models.CharField(max_length=255, null=True, verbose_name='title'),
        ),
    ]
