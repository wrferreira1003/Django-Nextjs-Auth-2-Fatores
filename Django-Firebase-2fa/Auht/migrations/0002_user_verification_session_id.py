# Generated by Django 5.0.1 on 2024-01-21 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auht', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='verification_session_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
