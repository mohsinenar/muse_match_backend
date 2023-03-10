# Generated by Django 3.2.18 on 2023-02-28 23:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_rename_song_track_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileView',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('viewed_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='viewed', to='profiles.userprofile')),
                ('viewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='views', to='profiles.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Pass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('passed_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='passes_received', to='profiles.userprofile')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='passes_given', to='profiles.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('matched_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matched_with', to='profiles.userprofile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches', to='profiles.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('liked_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes_received', to='profiles.userprofile')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes_given', to='profiles.userprofile')),
            ],
        ),
    ]
