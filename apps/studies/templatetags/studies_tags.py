"""Template tags for studies app."""
from django import template

from apps.studies.drive_urls import sanitize_drive_folder_url

register = template.Library()


@register.filter
def trusted_drive_url(value):
    """Return an allowlisted Drive/Docs URL, or empty string."""
    return sanitize_drive_folder_url(value)


@register.filter
def submission_number_display(value):
    """Return submission number or 'Pending' (never None or 'None')."""
    if value is None:
        return 'Pending'
    s = str(value).strip()
    if not s or s.lower() == 'none':
        return 'Pending'
    return value
