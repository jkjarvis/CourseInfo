# Generated by Django 3.0.4 on 2020-04-28 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20200427_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='rating',
            field=models.IntegerField(),
        ),
    ]