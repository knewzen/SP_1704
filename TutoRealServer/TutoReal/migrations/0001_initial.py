# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 10:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beacon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('major', models.PositiveIntegerField()),
                ('minor', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='チュートリアルの名前')),
                ('image_path', models.ImageField(upload_to='', verbose_name='サムネイル')),
                ('beacon', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='TutoReal.Beacon')),
            ],
        ),
    ]