# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-10 17:09
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('signIn', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offspring',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullNameOfOffspring', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Refugee',
            fields=[
                ('ID', models.CharField(max_length=16, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric')])),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('nationality', models.CharField(max_length=50)),
                ('refImage', models.FileField(upload_to='Images/')),
                ('maritalStatus', models.CharField(choices=[('M', 'Married'), ('S', 'Single')], default='S', max_length=1)),
                ('fullNameOfSpouse', models.CharField(max_length=100)),
                ('numOfOffspring', models.IntegerField()),
                ('fullNameOfFather', models.CharField(max_length=100)),
                ('fullNameOfMother', models.CharField(max_length=100)),
                ('Comments', models.CharField(max_length=500)),
                ('bID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='signIn.Benefactor')),
                ('fullNameOfOffspring', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bo.Offspring')),
            ],
        ),
    ]