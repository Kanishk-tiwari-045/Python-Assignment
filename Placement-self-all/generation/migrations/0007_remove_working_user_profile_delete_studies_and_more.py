# Generated by Django 5.0.6 on 2024-06-12 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('generation', '0006_studies_working'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='working',
            name='user_profile',
        ),
        migrations.DeleteModel(
            name='Studies',
        ),
        migrations.DeleteModel(
            name='Working',
        ),
    ]
