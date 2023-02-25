# Generated by Django 4.1.7 on 2023-02-25 17:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('followers', models.ManyToManyField(related_name='following_artists', to='profiles.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='MusicGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, upload_to='music_genre_images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('artist', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.artist')),
                ('genres', models.ManyToManyField(to='profiles.musicgenre')),
            ],
        ),
        migrations.CreateModel(
            name='MusicPreferencesProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artists', models.ManyToManyField(to='profiles.artist')),
                ('genres', models.ManyToManyField(blank=True, to='profiles.musicgenre')),
                ('songs', models.ManyToManyField(to='profiles.song')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='music_preferences', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='artist',
            name='genres',
            field=models.ManyToManyField(to='profiles.musicgenre'),
        ),
    ]
