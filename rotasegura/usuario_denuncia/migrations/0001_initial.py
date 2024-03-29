# Generated by Django 2.2.1 on 2019-06-03 04:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('denuncias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsuarioDenuncia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.CharField(max_length=1000)),
                ('latitude', models.CharField(max_length=100)),
                ('longitude', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('denuncia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario_denuncia', to='denuncias.Denuncia')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario_denuncia', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
