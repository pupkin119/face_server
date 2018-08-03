# Generated by Django 2.1 on 2018-08-03 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20180622_1012'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client_imgs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('encoded_image', models.CharField(max_length=245000)),
            ],
        ),
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_id', models.UUIDField()),
                ('restaurant_id', models.UUIDField()),
                ('created_at', models.DateTimeField(verbose_name='date created')),
                ('updated_at', models.DateTimeField(verbose_name='date updated')),
            ],
        ),
        migrations.DeleteModel(
            name='CreateId',
        ),
        migrations.AddField(
            model_name='client_imgs',
            name='client_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Clients'),
        ),
    ]
