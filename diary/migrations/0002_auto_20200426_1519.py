# Generated by Django 2.2.2 on 2020-04-26 06:19

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('diary', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Dairy',
            new_name='Diary',
        ),
    ]
