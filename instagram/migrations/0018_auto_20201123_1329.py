# Generated by Django 3.1.3 on 2020-11-23 10:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('instagram', '0017_auto_20201123_0741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='author',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
