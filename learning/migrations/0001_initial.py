# Generated by Django 2.0.5 on 2018-06-25 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WriteErrorToDb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module', models.CharField(max_length=40)),
                ('client_id', models.UUIDField()),
                ('error_id', models.IntegerField()),
            ],
        ),
    ]
