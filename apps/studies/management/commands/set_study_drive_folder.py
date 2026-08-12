"""
Point local Study rows at a Nicholls Google Drive materials folder.

Phase 1: writes URL/id metadata only — does not call Google APIs.
Synthetic-safe: prints study titles and counts, not participant data.
"""
from django.core.management.base import BaseCommand
from django.db.models import Q

from apps.accounts.models import User
from apps.studies.models import Study

DEFAULT_DRIVE_URL = (
    "https://drive.google.com/drive/folders/1jGaOtprui6PUq7r5W6qR6QYC9sRRXQpG"
)
DEFAULT_DRIVE_ID = "1jGaOtprui6PUq7r5W6qR6QYC9sRRXQpG"


class Command(BaseCommand):
    help = "Set drive_folder_url / drive_folder_id on studies owned by a researcher email."

    def add_arguments(self, parser):
        parser.add_argument(
            "--email",
            default="christopher.castille@nicholls.edu",
            help="Researcher email whose studies get the Drive link",
        )
        parser.add_argument(
            "--url",
            default=DEFAULT_DRIVE_URL,
            help="Google Drive folder URL to store on each study",
        )
        parser.add_argument(
            "--folder-id",
            default=DEFAULT_DRIVE_ID,
            help="Google Drive folder id (optional companion field)",
        )
        parser.add_argument(
            "--dry-run",
            action="store_true",
            help="Print what would change without writing",
        )

    def handle(self, *args, **options):
        email = options["email"]
        url = options["url"]
        folder_id = options["folder_id"]
        dry_run = options["dry_run"]

        researcher = User.objects.filter(email__iexact=email).first()
        if not researcher:
            self.stderr.write(self.style.ERROR(f"No user with email {email}"))
            return

        studies = Study.objects.filter(
            Q(researcher=researcher)
            | Q(protocol_submissions__co_investigator_users=researcher)
            | Q(protocol_submissions__co_investigators__icontains=email)
        ).distinct().order_by("title")

        count = studies.count()
        self.stdout.write(f"Researcher: {researcher.email}  studies={count}")
        self.stdout.write(f"Drive URL: {url}")
        self.stdout.write(f"Folder id: {folder_id}")

        if dry_run:
            for s in studies:
                self.stdout.write(f"  would update: {s.title}")
            self.stdout.write(self.style.WARNING("Dry run — no changes written."))
            return

        updated = studies.update(drive_folder_url=url, drive_folder_id=folder_id)
        self.stdout.write(self.style.SUCCESS(f"Updated {updated} study row(s)."))
        for s in studies:
            self.stdout.write(f"  linked: {s.title}")
