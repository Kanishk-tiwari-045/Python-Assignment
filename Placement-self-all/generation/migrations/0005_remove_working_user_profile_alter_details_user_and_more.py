# Generated by Django 5.0.6 on 2024-06-12 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generation', '0004_rename_profile_details_rename_education_studies_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='working',
            name='user_profile',
        ),
        migrations.AlterField(
            model_name='details',
            name='user',
            field=models.CharField(max_length=30),
        ),
        migrations.DeleteModel(
            name='Studies',
        ),
        migrations.DeleteModel(
            name='Working',
        ),
    ]
