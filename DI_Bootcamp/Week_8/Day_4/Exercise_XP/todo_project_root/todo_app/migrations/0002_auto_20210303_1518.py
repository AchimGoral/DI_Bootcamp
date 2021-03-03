# Generated by Django 3.1.7 on 2021-03-03 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='todos',
            field=models.ManyToManyField(related_name='all_todo', to='todo_app.Todo'),
        ),
        migrations.RemoveField(
            model_name='category',
            name='name',
        ),
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.CharField(default='no category', max_length=100),
        ),
    ]