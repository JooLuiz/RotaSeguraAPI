# Generated by Django 2.2.7 on 2019-12-01 17:06

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190930_2031'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, default='defaultAvatar.jpg', null=True, upload_to=users.models.User.upload_to),
        ),
        migrations.AddField(
            model_name='user',
            name='background',
            field=models.ImageField(blank=True, default='defaultBackground.jpg', null=True, upload_to=users.models.User.upload_to_background),
        ),
    ]
