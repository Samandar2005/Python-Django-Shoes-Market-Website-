# Generated by Django 3.1 on 2022-06-07 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20220607_1536'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Companiy',
            new_name='Company',
        ),
        migrations.RenameField(
            model_name='shoes',
            old_name='сompaniy',
            new_name='company',
        ),
    ]
