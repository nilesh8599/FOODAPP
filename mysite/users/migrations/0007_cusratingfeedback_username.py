# Generated by Django 4.2 on 2023-08-06 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_remove_cusorders_id_alter_cusorders_order_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='cusratingfeedback',
            name='username',
            field=models.CharField(default='username', max_length=200),
        ),
    ]