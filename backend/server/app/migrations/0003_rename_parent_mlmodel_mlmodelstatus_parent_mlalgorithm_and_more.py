# Generated by Django 5.1.1 on 2024-09-30 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_abtest'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mlmodelstatus',
            old_name='parent_mlmodel',
            new_name='parent_mlalgorithm',
        ),
        migrations.RenameField(
            model_name='mlrequest',
            old_name='parent_mlmodel',
            new_name='parent_mlalgorithm',
        ),
    ]
