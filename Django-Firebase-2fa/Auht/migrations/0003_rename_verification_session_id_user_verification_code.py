# Generated by Django 5.0.1 on 2024-01-21 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Auht', '0002_user_verification_session_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='verification_session_id',
            new_name='verification_code',
        ),
    ]
