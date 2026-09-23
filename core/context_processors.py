import re

from contact.models import Contact
from footer.models import Footer
from header_navigation.models import Header


def site_header(request):
    return {'header': Header.objects.prefetch_related('nav_items').first()}


def floating_contact(request):
    contact = Contact.objects.prefetch_related('methods').first()
    whatsapp_number = ''
    call_number = ''
    if contact:
        for method in contact.methods.all():
            digits = re.sub(r'\D', '', method.value)
            if method.label == 'WhatsApp' and digits:
                whatsapp_number = digits
            elif method.label == 'Call' and digits:
                call_number = digits

    return {
        'floating_whatsapp': whatsapp_number,
        'floating_call': call_number,
    }


def site_footer(request):
    footer = Footer.objects.prefetch_related('links', 'social_links').first()
    quick_links = []
    business_links = []
    if footer:
        for link in footer.links.all():
            (quick_links if link.column == 'quick_links' else business_links).append(link)

    return {
        'footer': footer,
        'footer_quick_links': quick_links,
        'footer_business_links': business_links,
    }
