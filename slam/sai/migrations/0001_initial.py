# Generated by Django 3.1.7 on 2021-06-26 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sai',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('rel', models.CharField(max_length=15)),
                ('impression', models.CharField(max_length=15)),
                ('memory', models.CharField(max_length=100)),
                ('honest', models.CharField(max_length=100)),
            ],
        ),
    ]
