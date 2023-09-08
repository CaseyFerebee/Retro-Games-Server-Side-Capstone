# Generated by Django 4.2.5 on 2023-09-08 15:40

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
            name='Condition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Console',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('releaseDate', models.DateField()),
                ('description', models.TextField()),
                ('condition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='condition_of_console', to='retroapi.condition')),
            ],
        ),
        migrations.CreateModel(
            name='Controller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('releaseDate', models.DateField()),
                ('description', models.TextField()),
                ('condition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='condition_of_controller', to='retroapi.condition')),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('releaseDate', models.DateField()),
                ('publisher', models.CharField(max_length=255)),
                ('developer', models.CharField(max_length=255)),
                ('modes', models.CharField(max_length=255)),
                ('condition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='condition_of_game', to='retroapi.condition')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consoles', models.ManyToManyField(to='retroapi.console')),
                ('controllers', models.ManyToManyField(to='retroapi.controller')),
                ('games', models.ManyToManyField(to='retroapi.game')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='genre_of_game', to='retroapi.genre'),
        ),
    ]
