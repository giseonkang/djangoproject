# Generated by Django 3.2.6 on 2021-08-03 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_auto_20210803_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='price',
            field=models.IntegerField(default=None, verbose_name='PRICE'),
        ),
    ]