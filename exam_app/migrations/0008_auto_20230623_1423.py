# Generated by Django 2.2.4 on 2023-06-23 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam_app', '0007_remove_player_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
    ]
