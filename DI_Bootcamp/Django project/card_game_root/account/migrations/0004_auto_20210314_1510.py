# Generated by Django 3.1.7 on 2021-03-14 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20210314_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.URLField(default='https://www.elegantthemes.com/blog/wp-content/uploads/2020/02/000-404.png', max_length=254),
        ),
    ]
