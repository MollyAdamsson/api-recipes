# Generated by Django 3.2.18 on 2023-04-14 08:53

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('followers', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='followers',
            new_name='Follower',
        ),
    ]
