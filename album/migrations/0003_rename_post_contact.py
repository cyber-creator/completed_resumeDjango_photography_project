# Generated by Django 4.1.1 on 2022-09-19 23:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0002_post'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Contact',
        ),
    ]