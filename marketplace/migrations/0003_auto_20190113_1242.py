# Generated by Django 2.1.5 on 2019-01-13 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0002_auto_20190113_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='inventory_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]