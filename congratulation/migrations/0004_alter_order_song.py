# Generated by Django 3.2.4 on 2021-06-14 12:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('congratulation', '0003_alter_order_song'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='song',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='congratulation.song', verbose_name='Песня'),
        ),
    ]
