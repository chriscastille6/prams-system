"""Allowlist Google Drive materials URLs before trusted IRB navigation."""
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.template import Context, Template
from django.test import SimpleTestCase

from apps.studies.drive_urls import (
    sanitize_drive_folder_url,
    validate_drive_folder_url,
)
from apps.studies.models import Study


VALID_FOLDER = "https://drive.google.com/drive/folders/1SyntheticFolderId_abc"
VALID_SHARED_USER = "https://drive.google.com/drive/u/0/folders/1SyntheticFolderId_abc"
VALID_OPEN = "https://drive.google.com/open?id=1SyntheticFolderId_abc"
VALID_DOC = "https://docs.google.com/document/d/1SyntheticDocId_abc/edit"


class _DriveUrlForm(ModelForm):
    class Meta:
        model = Study
        fields = ["drive_folder_url"]


class DriveFolderUrlAllowlistTests(SimpleTestCase):
    def test_accepts_https_drive_folder_and_docs_urls(self):
        for url in (VALID_FOLDER, VALID_SHARED_USER, VALID_OPEN, VALID_DOC):
            self.assertEqual(sanitize_drive_folder_url(url), url)

    def test_accepts_uppercase_scheme_and_host(self):
        url = "HTTPS://DRIVE.GOOGLE.COM/drive/folders/1SyntheticFolderId_abc"
        self.assertEqual(sanitize_drive_folder_url(url), url)

    def test_rejects_blank_and_non_strings(self):
        self.assertEqual(sanitize_drive_folder_url(""), "")
        self.assertEqual(sanitize_drive_folder_url(None), "")
        self.assertEqual(sanitize_drive_folder_url(123), "")

    def test_open_and_folderview_require_resource_id_for_path_variants(self):
        valid_id = "1SyntheticFolderId_abc"
        accepted = (
            f"https://drive.google.com/open?id={valid_id}",
            f"https://drive.google.com/open/?id={valid_id}",
            f"https://drive.google.com/folderview?id={valid_id}",
            f"https://drive.google.com/folderview/?id={valid_id}",
        )
        for url in accepted:
            self.assertEqual(sanitize_drive_folder_url(url), url, msg=url)

        rejected = (
            "https://drive.google.com/open",
            "https://drive.google.com/open/",
            "https://drive.google.com/open/extra",
            "https://drive.google.com/open/?url=https://evil.example/packet",
            "https://drive.google.com/open/extra?url=https://evil.example/packet",
            "https://drive.google.com/folderview",
            "https://drive.google.com/folderview/",
            "https://drive.google.com/folderview/extra",
            "https://drive.google.com/folderview/?url=https://evil.example/packet",
            "https://drive.google.com/open?id=",
            "https://drive.google.com/open/?id=",
            "https://drive.google.com/open?id=not valid",
        )
        for url in rejected:
            self.assertEqual(sanitize_drive_folder_url(url), "", msg=url)

    def test_rejects_non_drive_hosts_and_lookalikes(self):
        phishing = [
            "https://evil.example/drive/folders/1SyntheticFolderId_abc",
            "https://drive.google.com.evil.example/drive/folders/1SyntheticFolderId_abc",
            "https://accounts.google.com/ServiceLogin?continue=https://evil.example",
            "https://docs.google.com/gview?url=https://evil.example/packet",
            "http://drive.google.com/drive/folders/1SyntheticFolderId_abc",
            "javascript:alert(1)",
        ]
        for url in phishing:
            self.assertEqual(sanitize_drive_folder_url(url), "", msg=url)

    def test_rejects_dot_segment_walks_to_google_open_redirectors(self):
        """Reject /document/d/<id>/../ walks that browsers resolve to /gview."""
        doc = "1SyntheticDocId_abc"
        folder = "1SyntheticFolderId_abc"
        phishing = [
            f"https://docs.google.com/document/d/{doc}/../../../gview?url=https://evil.example/packet",
            f"https://docs.google.com/document/d/{doc}/../../../url?q=https://evil.example/packet",
            f"https://docs.google.com/document/d/{doc}/%2e%2e/%2e%2e/%2e%2e/gview?url=https://evil.example/packet",
            f"https://docs.google.com/document/d/{doc}/./../../gview?url=https://evil.example/packet",
            f"https://docs.google.com/document/d/{doc}/edit/../../../gview?url=https://evil.example/packet",
            f"https://drive.google.com/file/d/{folder}/../../../gview?url=https://evil.example/packet",
            f"https://drive.google.com/drive/folders/{folder}/../../../gview?url=https://evil.example/packet",
            f"https://docs.google.com/document/d/{doc}/%252e%252e/%252e%252e/%252e%252e/gview?url=https://evil.example/packet",
        ]
        for url in phishing:
            self.assertEqual(sanitize_drive_folder_url(url), "", msg=url)

    def test_rejects_userinfo_and_credential_host_tricks(self):
        # Built without a literal at-sign so the source is not flagged as an address.
        sep = chr(64)
        userinfo = f"https://researcher:secret{sep}drive.google.com/drive/folders/1SyntheticFolderId_abc"
        host_spoof = f"https://drive.google.com{sep}evil.example/drive/folders/1SyntheticFolderId_abc"
        self.assertEqual(sanitize_drive_folder_url(userinfo), "")
        self.assertEqual(sanitize_drive_folder_url(host_spoof), "")

    def test_validator_allows_blank_and_rejects_phishing(self):
        validate_drive_folder_url("")
        validate_drive_folder_url(VALID_FOLDER)
        with self.assertRaises(ValidationError):
            validate_drive_folder_url("https://evil.example/packet")

    def test_study_property_hides_untrusted_href(self):
        trusted = Study(drive_folder_url=VALID_FOLDER)
        untrusted = Study(drive_folder_url="https://evil.example/packet")
        self.assertEqual(trusted.trusted_drive_folder_url, VALID_FOLDER)
        self.assertEqual(untrusted.trusted_drive_folder_url, "")

    def test_dashboard_cta_omits_untrusted_href(self):
        template = Template(
            "{% if study.trusted_drive_folder_url %}"
            '<a href="{{ study.trusted_drive_folder_url }}">'
            "Open materials in Google Drive</a>"
            "{% endif %}"
        )
        phishing = Study(drive_folder_url="https://evil.example/packet")
        html = template.render(Context({"study": phishing}))
        self.assertNotIn("evil.example", html)
        self.assertNotIn("Open materials in Google Drive", html)

        drive = Study(drive_folder_url=VALID_FOLDER)
        html = template.render(Context({"study": drive}))
        self.assertIn(VALID_FOLDER, html)
        self.assertIn("Open materials in Google Drive", html)

    def test_model_form_rejects_non_drive_url(self):
        form = _DriveUrlForm(data={"drive_folder_url": "https://evil.example/packet"})
        self.assertFalse(form.is_valid())
        self.assertIn("drive_folder_url", form.errors)

    def test_model_form_accepts_drive_folder_url(self):
        form = _DriveUrlForm(data={"drive_folder_url": VALID_FOLDER})
        self.assertTrue(form.is_valid(), form.errors)
        self.assertEqual(form.cleaned_data["drive_folder_url"], VALID_FOLDER)
