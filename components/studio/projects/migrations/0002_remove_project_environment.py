# Generated by Django 2.2.13 on 2020-09-10 21:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='environment',
        ),
    ]
