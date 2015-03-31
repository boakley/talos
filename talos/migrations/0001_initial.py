# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('path', models.CharField(max_length=2048, null=True)),
                ('name', models.CharField(max_length=256)),
                ('collection_type', models.CharField(max_length=8, choices=[(b'library', b'Library'), (b'resource', b'Resource file'), (b'suite', b'Test suite')])),
                ('version', models.CharField(max_length=12, blank=True)),
                ('scope', models.CharField(default=b'global', max_length=6, choices=[(b'global', b'Global'), (b'suite', b'Test suite'), (b'test', b'Test case')])),
                ('namedargs', models.CharField(max_length=2048, blank=True)),
                ('doc_format', models.CharField(default=b'ROBOT', max_length=10, choices=[(b'HTML', b'HTML'), (b'TEXT', b'Plain text'), (b'ROBOT', b'Robot'), (b'reST', b'reStructured Text')])),
                ('doc', models.TextField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('args', models.CharField(max_length=256)),
                ('doc', models.TextField(verbose_name=b'Documentation', blank=True)),
                ('collection', models.ForeignKey(to='talos.Collection')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('root', models.CharField(max_length=1024)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Testcase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('doc', models.TextField(verbose_name=b'Documentation', blank=True)),
                ('collection', models.ForeignKey(to='talos.Collection')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='collection',
            name='project',
            field=models.ForeignKey(to='talos.Project', null=True),
            preserve_default=True,
        ),
    ]
