# Generated by Django 2.0.3 on 2018-08-24 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_auto_20180821_1559'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='partnode',
        ),
    ]
