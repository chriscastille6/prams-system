# Allowlist validator for Study.drive_folder_url (no schema change)

from django.db import migrations, models

from apps.studies.drive_urls import validate_drive_folder_url


class Migration(migrations.Migration):

    dependencies = [
        ("studies", "0036_study_drive_folder_fields"),
    ]

    operations = [
        migrations.AlterField(
            model_name="study",
            name="drive_folder_url",
            field=models.URLField(
                blank=True,
                help_text=(
                    "Nicholls Google Drive folder for study/protocol materials "
                    "(https drive.google.com / docs.google.com only)"
                ),
                validators=[validate_drive_folder_url],
            ),
        ),
    ]
