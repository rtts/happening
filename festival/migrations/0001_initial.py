# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-03 19:27
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.PositiveIntegerField(blank=True, verbose_name='positie')),
                ('type', models.CharField(choices=[('photo', 'Foto'), ('video', 'Video'), ('text', 'Tekst')], help_text='Kies hier het type element. Een foto-element lat een foto zien, een video element een video, etc.', max_length=16)),
                ('image', models.ImageField(blank=True, upload_to='', verbose_name='afbeelding')),
                ('video', embed_video.fields.EmbedVideoField(blank=True, help_text='Plak hier een YouTube of Vimeo link')),
                ('text', ckeditor.fields.RichTextField(blank=True, verbose_name='tekst')),
            ],
            options={
                'verbose_name_plural': 'elementen',
                'ordering': ['position'],
            },
        ),
    ]
