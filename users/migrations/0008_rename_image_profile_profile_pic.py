# Generated by Django 3.2 on 2021-07-31 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_profile_stream'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='image',
            new_name='profile_pic',
        ),
    ]
