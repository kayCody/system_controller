# Generated by Django 4.1.2 on 2023-12-18 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='members_id'),
        ),
    ]
