# Generated by Django 3.1.5 on 2021-01-21 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petdata', '0002_createpet_owner_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createpet',
            name='owner_phone',
            field=models.CharField(max_length=255),
        ),
    ]
