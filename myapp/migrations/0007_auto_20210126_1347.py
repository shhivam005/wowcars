# Generated by Django 3.1 on 2021-01-26 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20210126_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='kilometers_driven',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_price',
            field=models.CharField(default='', max_length=25),
        ),
    ]
