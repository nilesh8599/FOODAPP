# Generated by Django 4.2 on 2023-04-10 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=200)),
                ('item_des', models.CharField(max_length=200)),
                ('item_price', models.IntegerField()),
            ],
        ),
    ]
