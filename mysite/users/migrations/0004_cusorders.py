# Generated by Django 4.2 on 2023-08-01 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_cusratingfeedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='CusOrders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_code', models.IntegerField()),
                ('user', models.CharField(max_length=200)),
            ],
        ),
    ]