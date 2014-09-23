# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HTMLChunk',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.SlugField(verbose_name='Code')),
                ('body_en', models.TextField(default=b'', verbose_name='Body', blank=True)),
                ('body_es', models.TextField(default=b'', verbose_name='Body', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
