# Generated by Django 4.2.6 on 2023-10-12 05:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tg_name', models.CharField(max_length=20)),
                ('Tg_priority', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('Description', models.CharField(max_length=500)),
                ('Timeline', models.DateTimeField()),
                ('Status', models.CharField(default='ot', max_length=2)),
                ('Is_completed', models.BinaryField(default=False)),
                ('Tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TaskManager.tag')),
            ],
        ),
    ]
