# Generated by Django 4.2 on 2023-08-02 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_cusorders'),
    ]

    operations = [
        migrations.AddField(
            model_name='cusorders',
            name='order_id',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='cusorders',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
