# Generated by Django 4.2 on 2023-07-11 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0006_item_for_user_item_prod_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=200)),
                ('prod_ref', models.IntegerField(default=100)),
                ('item_name', models.CharField(max_length=200)),
                ('op_type', models.CharField(max_length=100)),
            ],
        ),
    ]
