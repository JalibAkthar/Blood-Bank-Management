# Generated by Django 4.2.4 on 2023-11-26 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BloodUserSide', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoginDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('L_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('L_Email', models.EmailField(blank=True, max_length=100, null=True)),
                ('L_Password', models.CharField(blank=True, max_length=100, null=True)),
                ('C_Password', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
