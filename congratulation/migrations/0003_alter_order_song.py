# Generated by Django 3.2.4 on 2021-06-14 12:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('congratulation', '0002_auto_20210614_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='song',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='congratulation.song', verbose_name='Песня'),
        ),
    ]
