# Generated by Django 2.0.3 on 2018-09-05 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0004_auto_20180826_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='prize',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='prize/%Y/%m', verbose_name='照片'),
        ),
    ]
