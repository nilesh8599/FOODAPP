# Generated by Django 4.2.3 on 2023-07-12 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='user_type',
            field=models.CharField(default='users', max_length=200),
        ),
    ]
