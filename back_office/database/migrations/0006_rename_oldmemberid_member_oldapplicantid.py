# Generated by Django 4.1.2 on 2024-03-01 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0005_formtoken_member_oldmemberid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='oldMemberId',
            new_name='oldApplicantId',
        ),
    ]