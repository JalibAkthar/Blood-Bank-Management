# Generated by Django 4.2.4 on 2023-11-27 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BloodUserSide', '0002_logindb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logindb',
            name='C_Password',
        ),
        migrations.AddField(
            model_name='logindb',
            name='L_Mobile',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
