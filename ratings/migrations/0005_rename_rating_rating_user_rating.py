# Generated by Django 3.2.18 on 2023-04-22 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0004_rating_rating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='rating',
            new_name='user_rating',
        ),
    ]
