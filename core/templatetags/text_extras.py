from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def last_word_initial(value):
    """'Our Vision' -> 'V'. Used for the Vision & Mission watermark letter."""
    words = (value or '').split()
    return words[-1][0].upper() if words else ''


PLATFORM_ABBREVIATIONS = {
    'facebook': 'f',
    'instagram': 'ig',
    'youtube': 'yt',
    'twitter': 'x',
    'linkedin': 'in',
    'whatsapp': 'wa',
}


@register.filter
def platform_abbr(value):
    """'Instagram' -> 'ig'. Used for the social icon circles."""
    key = (value or '').strip().lower()
    if key in PLATFORM_ABBREVIATIONS:
        return PLATFORM_ABBREVIATIONS[key]
    return value[:2].lower() if value else ''


PLATFORM_ICONS = {
    'facebook': (
        '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">'
        '<path d="M22 12.06C22 6.5 17.52 2 12 2S2 6.5 2 12.06C2 17.08 5.66 21.23 10.44 22v-7.03H7.9v-2.91h2.54V9.85c0-2.5 1.49-3.89 3.77-3.89 1.09 0 2.24.2 2.24.2v2.46h-1.26c-1.24 0-1.63.77-1.63 1.56v1.88h2.78l-.44 2.91h-2.34V22C18.34 21.23 22 17.08 22 12.06z"/>'
        '</svg>'
    ),
    'instagram': (
        '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true">'
        '<rect x="3" y="3" width="18" height="18" rx="5"/>'
        '<circle cx="12" cy="12" r="4.2"/>'
        '<circle cx="17.4" cy="6.6" r="1.1" fill="currentColor" stroke="none"/>'
        '</svg>'
    ),
    'youtube': (
        '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">'
        '<path d="M9 7.3v9.4a.6.6 0 0 0 .9.53l8.2-4.7a.6.6 0 0 0 0-1.06l-8.2-4.7A.6.6 0 0 0 9 7.3z"/>'
        '</svg>'
    ),
    'whatsapp': (
        '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">'
        '<path d="M12 2a10 10 0 0 0-8.6 15L2 22l5.2-1.4A10 10 0 1 0 12 2zm5.8 14.2c-.24.68-1.4 1.3-1.96 1.38-.5.08-1.14.11-1.83-.11-.42-.13-.97-.3-1.66-.6-2.93-1.27-4.84-4.24-4.99-4.44-.15-.2-1.2-1.6-1.2-3.05s.75-2.17 1.02-2.47c.26-.3.58-.37.77-.37h.55c.18 0 .42-.03.64.49.24.55.8 1.9.87 2.04.07.14.12.3.02.49-.1.19-.15.3-.3.46-.15.17-.31.37-.44.5-.15.14-.3.3-.13.6.17.3.76 1.25 1.63 2.02 1.12 1 2.06 1.31 2.36 1.46.3.14.48.12.65-.07.2-.22.72-.83.91-1.12.2-.29.39-.24.66-.14.27.1 1.7.8 1.99.95.3.14.49.22.56.34.08.13.08.75-.16 1.43z"/>'
        '</svg>'
    ),
    'twitter': (
        '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">'
        '<path d="M3 3l7.4 9.9L3.2 21h2.3l6.2-6.7L16.9 21H21l-7.7-10.3L20.1 3h-2.3l-5.8 6.2L8 3H3z"/>'
        '</svg>'
    ),
    'linkedin': (
        '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">'
        '<path d="M6.94 5a2 2 0 1 1-4 0 2 2 0 0 1 4 0zM3.2 8.75h3.5V21H3.2V8.75zM9.4 8.75h3.35v1.68h.05c.47-.87 1.6-1.79 3.3-1.79 3.53 0 4.18 2.32 4.18 5.34V21h-3.5v-5.4c0-1.29-.02-2.96-1.8-2.96-1.8 0-2.08 1.4-2.08 2.86V21H9.4V8.75z"/>'
        '</svg>'
    ),
}


@register.filter
def social_icon(value):
    """Real brand icon SVG for a platform name, falling back to its initials."""
    key = (value or '').strip().lower()
    if key in PLATFORM_ICONS:
        return mark_safe(PLATFORM_ICONS[key])
    return platform_abbr(value)
