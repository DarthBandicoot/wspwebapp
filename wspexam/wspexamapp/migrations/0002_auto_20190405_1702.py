# Generated by Django 2.2 on 2019-04-05 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wspexamapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='examresults',
            name='exam',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='wspexamapp.Exam'),
        ),
        migrations.AddField(
            model_name='examresults',
            name='result',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
