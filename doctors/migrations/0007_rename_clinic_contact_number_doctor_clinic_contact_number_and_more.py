# Generated by Django 5.1.6 on 2025-03-04 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0006_rename_clinic_number_doctor_clinic_contact_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='clinic_contact_number',
            new_name='clinic_Contact_Number',
        ),
        migrations.AddField(
            model_name='doctor',
            name='clinic_city',
            field=models.TextField(blank=True, max_length=15, null=True),
        ),
    ]
