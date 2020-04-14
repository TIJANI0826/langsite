# Generated by Django 3.0 on 2019-11-29 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=250)),
                ('name', models.CharField(max_length=250)),
                ('phone_number', models.CharField(max_length=250)),
                ('message', models.TextField(max_length=300)),
                ('sender', models.EmailField(max_length=254)),
                ('subject', models.CharField(default='user', max_length=250)),
                ('cc_myself', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='FormMasters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form_master_name', models.CharField(max_length=250)),
                ('class_for', models.CharField(max_length=250)),
            ],
        ),
    ]
