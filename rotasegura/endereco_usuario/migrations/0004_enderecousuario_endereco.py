# Generated by Django 2.2.1 on 2019-10-16 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endereco_usuario', '0003_auto_20190603_0131'),
    ]

    operations = [
        migrations.AddField(
            model_name='enderecousuario',
            name='endereco',
            field=models.CharField(max_length=600, null=True),
        ),
    ]
