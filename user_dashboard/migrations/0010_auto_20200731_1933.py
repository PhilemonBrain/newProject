# Generated by Django 3.0.8 on 2020-07-31 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_dashboard', '0009_activeapilist_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apilist',
            name='created_on',
        ),
        migrations.RemoveField(
            model_name='apilist',
            name='updated_on',
        ),
    ]
