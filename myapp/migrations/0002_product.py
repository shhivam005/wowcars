# Generated by Django 3.1 on 2021-01-25 12:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('product_description', models.CharField(max_length=1000)),
                ('product_price', models.IntegerField(default=0)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
