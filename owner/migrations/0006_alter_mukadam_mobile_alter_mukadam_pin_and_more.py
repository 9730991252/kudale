# Generated by Django 5.0.6 on 2024-07-06 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0005_vehicle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mukadam',
            name='mobile',
            field=models.IntegerField(max_length=100),
        ),
        migrations.AlterField(
            model_name='mukadam',
            name='pin',
            field=models.IntegerField(max_length=100),
        ),
        migrations.AlterField(
            model_name='mukadam',
            name='status',
            field=models.IntegerField(max_length=100),
        ),
        migrations.AlterField(
            model_name='taneg',
            name='taneg',
            field=models.FloatField(max_length=100),
        ),
    ]
