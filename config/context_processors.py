"""
Custom context processors for templates.
"""
from django.conf import settings


def site_settings(request):
    """Add site-wide settings to template context."""
    default_drive = (
        'https://drive.google.com/drive/folders/1jGaOtprui6PUq7r5W6qR6QYC9sRRXQpG'
    )
    return {
        'SITE_NAME': settings.SITE_NAME,
        'INSTITUTION_NAME': settings.INSTITUTION_NAME,
        'SITE_URL': settings.SITE_URL,
        'PLATFORM_SUPPORT_EMAIL': getattr(settings, 'PLATFORM_SUPPORT_EMAIL', ''),
        'COB_HSIRB_DRIVE_ROOT_URL': getattr(
            settings, 'COB_HSIRB_DRIVE_ROOT_URL', default_drive
        )
        or default_drive,
    }




