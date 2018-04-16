# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('choice_text', models.CharField(verbose_name='投票理由', max_length=200)),
                ('votes', models.IntegerField(verbose_name='投票数量', default=0)),
            ],
            options={
                'verbose_name': '投票',
                'verbose_name_plural': '投票',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('question_text', models.CharField(verbose_name='问题内容', max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
            options={
                'verbose_name': '问题',
                'verbose_name_plural': '问题',
            },
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(to='poll.Question'),
        ),
    ]
