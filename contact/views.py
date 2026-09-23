import json
import logging

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .models import Enquiry

logger = logging.getLogger(__name__)


@csrf_exempt
@require_POST
def submit_enquiry(request):
    if request.content_type == 'application/json':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'ok': False, 'error': 'Invalid JSON body'}, status=400)
    else:
        data = request.POST

    name = (data.get('name') or '').strip()
    if not name:
        return JsonResponse({'ok': False, 'error': 'Name is required'}, status=400)

    enquiry = Enquiry.objects.create(
        name=name,
        phone=(data.get('phone') or '').strip(),
        email=(data.get('email') or '').strip(),
        business_interest=(data.get('business') or '').strip(),
        message=(data.get('message') or '').strip(),
    )

    if getattr(settings, 'ENQUIRY_NOTIFY_EMAIL', ''):
        try:
            html_body = render_to_string('emails/enquiry_notification.html', {'enquiry': enquiry})
            email = EmailMultiAlternatives(
                subject=f'New enquiry from {enquiry.name} — SJR Groups website',
                body=strip_tags(html_body),
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[settings.ENQUIRY_NOTIFY_EMAIL],
            )
            email.attach_alternative(html_body, 'text/html')
            email.send(fail_silently=False)
        except Exception:
            logger.exception('Failed to send enquiry notification email')

    return JsonResponse({'ok': True, 'id': enquiry.pk}, status=201)
