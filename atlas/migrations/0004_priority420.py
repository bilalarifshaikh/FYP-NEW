# Generated by Django 5.1.5 on 2025-03-16 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atlas', '0003_finishedproduct'),
    ]

    operations = [
        migrations.CreateModel(
            name='Priority420',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(default='420', max_length=50)),
                ('part', models.CharField(max_length=50)),
                ('priority', models.IntegerField()),
            ],
        ),
    ]
