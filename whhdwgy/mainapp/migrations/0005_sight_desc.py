# Generated by Django 2.0.3 on 2018-08-17 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_sightimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='sight',
            name='desc',
            field=models.TextField(blank=True, null=True, verbose_name='简介'),
        ),
    ]
