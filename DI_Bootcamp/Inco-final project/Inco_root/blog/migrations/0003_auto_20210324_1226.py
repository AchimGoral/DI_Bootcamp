# Generated by Django 3.1.7 on 2021-03-24 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210324_1056'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='user',
            new_name='profile',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='user',
            new_name='profile',
        ),
        migrations.RemoveField(
            model_name='post',
            name='answers',
        ),
    ]
