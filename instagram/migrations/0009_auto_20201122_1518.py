# Generated by Django 3.1.3 on 2020-11-22 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0008_auto_20201122_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='caption',
            field=models.TextField(null=True),
        ),
    ]
