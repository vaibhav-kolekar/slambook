# Generated by Django 3.1.7 on 2021-06-27 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sai', '0002_auto_20210627_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sai',
            name='impression',
            field=models.CharField(max_length=100),
        ),
    ]
