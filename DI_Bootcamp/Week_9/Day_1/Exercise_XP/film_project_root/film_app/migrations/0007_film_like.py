# Generated by Django 3.1.7 on 2021-03-11 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film_app', '0006_auto_20210308_1827'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='like',
            field=models.IntegerField(default=0),
        ),
    ]
