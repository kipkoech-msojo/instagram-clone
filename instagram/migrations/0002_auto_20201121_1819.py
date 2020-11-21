# Generated by Django 3.1.3 on 2020-11-21 15:19

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('instagram', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='content',
        ),
        migrations.AddField(
            model_name='image',
            name='caption',
            field=models.CharField(max_length=3000, null=True),
        ),
        migrations.AddField(
            model_name='image',
            name='comment',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='image',
            name='image',
            field=cloudinary.models.CloudinaryField(default=True, max_length=255, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='image',
            name='image_name',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='image',
            name='likes',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_photo', cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image')),
                ('bio', models.TextField()),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]