# Generated by Django 3.0 on 2019-11-29 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('langapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactform',
            name='sender',
        ),
        migrations.AlterField(
            model_name='contactform',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
