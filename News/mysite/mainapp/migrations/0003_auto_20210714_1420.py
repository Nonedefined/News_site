# Generated by Django 2.2.12 on 2021-07-14 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20210713_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
    ]
