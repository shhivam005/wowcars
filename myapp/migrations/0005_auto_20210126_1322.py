# Generated by Django 3.1 on 2021-01-26 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20210126_1310'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='engine',
        ),
        migrations.AddField(
            model_name='product',
            name='fuel',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AlterField(
            model_name='product',
            name='transmission',
            field=models.CharField(default='Manual', max_length=20),
        ),
    ]