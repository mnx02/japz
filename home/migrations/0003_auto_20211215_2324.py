# Generated by Django 3.2.7 on 2021-12-15 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20211215_2302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='date',
        ),
        migrations.RemoveField(
            model_name='register',
            name='desc',
        ),
    ]