# Generated by Django 4.1.7 on 2023-02-25 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_artist_musicgenre_song_musicpreferencesprofile_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
