# Generated by Django 2.2 on 2019-04-05 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wspexamapp', '0002_auto_20190405_1702'),
    ]

    operations = [
        migrations.RenameField(
            model_name='examresults',
            old_name='result',
            new_name='total',
        ),
    ]
