# Generated manually for Phase 1 Drive materials links

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("studies", "0035_add_calendar_sync_and_sms_flags"),
    ]

    operations = [
        migrations.AddField(
            model_name="study",
            name="drive_folder_id",
            field=models.CharField(
                blank=True,
                help_text="Google Drive folder id (optional; used with drive_folder_url)",
                max_length=128,
            ),
        ),
        migrations.AddField(
            model_name="study",
            name="drive_folder_url",
            field=models.URLField(
                blank=True,
                help_text="Nicholls Google Drive folder for study/protocol materials (packets, CITI, consents)",
            ),
        ),
    ]
