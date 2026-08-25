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

# Entire path after unquote. A prefix .match() would accept
# /document/d/<id>/../../../gview (browsers then land on Google's
# /gview?url= and /url?q= open-redirectors). Optional single suffix covers
# /edit, /view, /preview. /open and /folderview are exact paths only.
_DRIVE_RESOURCE_PATH = re.compile(
    r"^("
    r"(?:/drive/(?:u/\d+/)?folders/[A-Za-z0-9_-]+"
    r"|/file/d/[A-Za-z0-9_-]+"
    r"|/document/d/[A-Za-z0-9_-]+"
    r"|/spreadsheets/d/[A-Za-z0-9_-]+"
    r"|/presentation/d/[A-Za-z0-9_-]+"
    r"|/forms/d/[A-Za-z0-9_-]+"
    r")(?:/[A-Za-z0-9_-]+)?"
    r"|/open"
    r"|/folderview"
    r")$",
    re.IGNORECASE,
)
_OPEN_OR_FOLDERVIEW_PATH = re.compile(r"^/(?:open|folderview)$", re.IGNORECASE)
_DRIVE_ID = re.compile(r"^[A-Za-z0-9_-]+$")
_MAX_UNQUOTE_ROUNDS = 5

DRIVE_URL_HELP = (
    "Must be an https Google Drive or Docs materials link "
    "(drive.google.com or docs.google.com)."
)


def _fully_unquote_path(path: str) -> str:
    """Decode percent-encoding until stable. '' if it never settles."""
    current = path
    for _ in range(_MAX_UNQUOTE_ROUNDS):
        decoded = unquote(current)
        if decoded == current:
            return current
        current = decoded
    return ""


def _normalize_url_path(path: str) -> str:
    """Unquote and collapse '//' so the allowlist can fullmatch the path.

    Dot-segments are rejected, not rewritten: a researcher URL that starts
    with /document/d/<id>/ and then walks upward must not be stored as a
    trusted materials href (browsers would then reach /gview or /url).
    """
    if not path or "\\" in path or "\x00" in path:
        return ""
    decoded = _fully_unquote_path(path)
    if not decoded or "\\" in decoded or "\x00" in decoded or "%" in decoded:
        return ""
    segments: list[str] = []
    for part in decoded.split("/"):
        if part == "":
            continue
        if part in (".", ".."):
            return ""
        segments.append(part)
    return "/" + "/".join(segments)


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

    path = _normalize_url_path(parsed.path or "")
    if not path or not _DRIVE_RESOURCE_PATH.fullmatch(path):
        return ""

    if _OPEN_OR_FOLDERVIEW_PATH.fullmatch(path):
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
