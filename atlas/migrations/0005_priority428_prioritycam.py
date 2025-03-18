# Generated by Django 5.1.5 on 2025-03-17 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atlas', '0004_priority420'),
    ]

    operations = [
        migrations.CreateModel(
            name='Priority428',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(default='428', max_length=50)),
                ('part', models.CharField(max_length=50)),
                ('priority', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PriorityCAM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(default='CAM', max_length=50)),
                ('part', models.CharField(max_length=50)),
                ('priority', models.IntegerField()),
            ],
        ),
    ]
