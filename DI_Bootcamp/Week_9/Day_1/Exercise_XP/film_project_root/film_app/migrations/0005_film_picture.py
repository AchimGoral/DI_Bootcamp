# Generated by Django 3.1.7 on 2021-03-08 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film_app', '0004_film_available_in_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='picture',
            field=models.URLField(default=0),
        ),
    ]
