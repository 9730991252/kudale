# Generated by Django 5.0.6 on 2024-07-06 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0006_alter_mukadam_mobile_alter_mukadam_pin_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
