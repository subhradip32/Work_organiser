# Generated by Django 4.2.6 on 2023-10-12 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TaskManager', '0002_tasks_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='Is_completed',
            field=models.BooleanField(default=False),
        ),
    ]
