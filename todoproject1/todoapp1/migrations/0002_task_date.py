# Generated by Django 3.2.16 on 2022-12-04 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1993-03-22'),
            preserve_default=False,
        ),
    ]
