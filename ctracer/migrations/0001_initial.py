# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('semester_text', models.CharField(max_length=100)),
                ('crn', models.IntegerField(default=100)),
                ('subject', models.CharField(max_length=100)),
                ('course_Number', models.IntegerField(default=100)),
                ('section', models.IntegerField(default=100)),
                ('title', models.CharField(max_length=100)),
            ],
        ),
    ]
