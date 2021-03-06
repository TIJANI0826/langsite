# Generated by Django 2.0.13 on 2020-04-04 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0003_auto_20200404_2051'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_on']},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='content',
            new_name='body',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='object_id',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='comment',
            name='created_on',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='comment',
            name='email',
            field=models.EmailField(default='none', max_length=254),
        ),
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.CharField(default='user', max_length=80),
            preserve_default=False,
        ),
    ]
