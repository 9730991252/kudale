# Generated by Django 3.2.6 on 2024-07-05 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Add_mukadam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mobile', models.IntegerField()),
                ('pin', models.IntegerField()),
                ('status', models.IntegerField()),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
