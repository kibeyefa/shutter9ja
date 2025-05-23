# Generated by Django 5.2 on 2025-04-18 04:31

import app.models
import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_entry_vote_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='photo_entry',
        ),
        migrations.AddField(
            model_name='entry',
            name='submitted_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2025, 4, 18, 4, 31, 8, 895479, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='entry',
            name='competition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.competition'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='photography_experience',
            field=models.CharField(choices=[('Beginer', 'Beginner'), ('Intermediate', 'Intermediate'), ('Professional', 'Professional')], max_length=255),
        ),
        migrations.AlterField(
            model_name='entry',
            name='profile_picture',
            field=models.ImageField(upload_to='static/uploads/entries/user_images/'),
        ),
        migrations.CreateModel(
            name='EntryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=app.models.entry_image_upload_path)),
                ('entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='app.entry')),
            ],
        ),
    ]
