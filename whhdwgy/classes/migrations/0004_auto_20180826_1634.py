# Generated by Django 2.0.3 on 2018-08-26 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0003_auto_20180826_1631'),
    ]

    operations = [
        migrations.RenameField(
            model_name='classimage',
            old_name='pclass',
            new_name='p_class',
        ),
        migrations.RenameField(
            model_name='prize',
            old_name='pclass',
            new_name='p_class',
        ),
    ]
