# Generated by Django 3.1.3 on 2020-11-22 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0005_auto_20201122_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='avatar.jpg', upload_to='profile_pictures'),
        ),
    ]
