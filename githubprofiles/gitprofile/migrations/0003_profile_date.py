# Generated by Django 3.2.7 on 2021-09-19 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gitprofile', '0002_profile_repository'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
