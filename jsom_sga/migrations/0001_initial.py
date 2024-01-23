# Generated by Django 4.2.7 on 2024-01-23 21:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peso', models.FloatField(blank=True, null=True)),
                ('altura', models.FloatField(blank=True, null=True)),
                ('data_nascimento', models.DateField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Treino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=90)),
                ('categoria', models.CharField(choices=[('Treino(A)', 'Treino-A'), ('Treino(B)', 'Treino-B'), ('Treino(C)', 'Treino-C'), ('Treino(D)', 'Treino-D'), ('Treino(E)', 'Treino-E')], max_length=9)),
                ('imagem', models.ImageField(blank=True, upload_to='pictures/%Y/%m/')),
                ('descricao', models.TextField(blank=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]