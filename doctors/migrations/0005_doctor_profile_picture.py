# Generated by Django 5.1.6 on 2025-02-26 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0004_delete_patient'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pictures/'),
        ),
    ]
