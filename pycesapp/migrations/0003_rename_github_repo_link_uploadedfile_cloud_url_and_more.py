# Generated by Django 5.0.1 on 2024-01-13 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pycesapp', '0002_remove_uploadedfile_file_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uploadedfile',
            old_name='github_repo_link',
            new_name='cloud_url',
        ),
        migrations.AddField(
            model_name='uploadedfile',
            name='repo_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='uploadedfile',
            name='zipfile',
            field=models.FileField(blank=True, upload_to='uploads/'),
        ),
    ]
