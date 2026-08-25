"""
Allowlist Google Drive materials URLs before they are stored or rendered.

Researchers can set Study.drive_folder_url. IRB dashboards label that value as
"Open materials in Google Drive", so a non-Drive href is a cross-role phishing
vector. Only https Drive/Docs resource URLs are trusted.
"""
from __future__ import annotations

import re
from urllib.parse import parse_qs, unquote, urlparse

from django.core.exceptions import ValidationError

ALLOWED_DRIVE_HOSTS = frozenset({
    "drive.google.com",
    "docs.google.com",
})

# Folder / file / Workspace document paths — not Google open-redirectors
# such as /gview?url= or /url?q=.
_DRIVE_RESOURCE_PATH = re.compile(
    r"^("
    r"/drive/(?:u/\d+/)?folders/[A-Za-z0-9_-]+"
    r"|/file/d/[A-Za-z0-9_-]+"
    r"|/document/d/[A-Za-z0-9_-]+"
    r"|/spreadsheets/d/[A-Za-z0-9_-]+"
    r"|/presentation/d/[A-Za-z0-9_-]+"
    r"|/forms/d/[A-Za-z0-9_-]+"
    r"|/open"
    r"|/folderview"
    r")(/|$)",
    re.IGNORECASE,
)
# Same prefix as the /open|/folderview alternatives above, including a trailing
# slash or extra path that .match() already accepts.
_OPEN_OR_FOLDERVIEW_PATH = re.compile(r"^/(?:open|folderview)(?:/|$)", re.IGNORECASE)
_DRIVE_ID = re.compile(r"^[A-Za-z0-9_-]+$")

DRIVE_URL_HELP = (
    "Must be an https Google Drive or Docs materials link "
    "(drive.google.com or docs.google.com)."
)


def sanitize_drive_folder_url(url: str | None) -> str:
    """Return url when it is an allowlisted Drive/Docs HTTPS resource, else ''."""
    if not url or not isinstance(url, str):
        return ""
    candidate = url.strip()
    if not candidate:
        return ""

    parsed = urlparse(candidate)
    if parsed.scheme.lower() != "https":
        return ""
    if parsed.username is not None or parsed.password is not None:
        return ""
    if parsed.port not in (None, 443):
        return ""

    host = (parsed.hostname or "").rstrip(".").lower()
    try:
        host = host.encode("idna").decode("ascii")
    except (UnicodeError, ValueError):
        return ""
    if host not in ALLOWED_DRIVE_HOSTS:
        return ""

    path = unquote(parsed.path or "")
    if not _DRIVE_RESOURCE_PATH.match(path):
        return ""

    if _OPEN_OR_FOLDERVIEW_PATH.match(path):
        folder_ids = parse_qs(parsed.query).get("id", [])
        if not folder_ids or not _DRIVE_ID.fullmatch(folder_ids[0]):
            return ""

    return candidate


def is_trusted_drive_folder_url(url: str | None) -> bool:
    return bool(sanitize_drive_folder_url(url))


def validate_drive_folder_url(value: str | None) -> None:
    """Django field validator: blank is allowed; non-Drive URLs are not."""
    if not value:
        return
    if not sanitize_drive_folder_url(value):
        raise ValidationError(DRIVE_URL_HELP, code="invalid_drive_url")
