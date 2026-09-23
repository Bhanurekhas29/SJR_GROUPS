from django.contrib import admin

from core.admin_base import SingletonModelAdmin
from .models import Footer, FooterLink, FooterSocialLink


class FooterLinkInline(admin.TabularInline):
    model = FooterLink
    extra = 1
    fields = ('column', 'label', 'url', 'order')


class FooterSocialLinkInline(admin.TabularInline):
    model = FooterSocialLink
    extra = 3
    fields = ('platform', 'url', 'order')


@admin.register(Footer)
class FooterAdmin(SingletonModelAdmin, admin.ModelAdmin):
    fields = (
        'logo',
        'brand_name',
        'tagline',
        'description',
        'phone',
        'email',
        'location',
        'copyright_text',
    )
    inlines = [FooterLinkInline, FooterSocialLinkInline]
