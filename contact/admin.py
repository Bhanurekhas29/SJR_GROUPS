from django.contrib import admin

from core.admin_base import SingletonModelAdmin
from .models import Contact, ContactMethod, Enquiry


class ContactMethodInline(admin.TabularInline):
    model = ContactMethod
    extra = 3
    fields = ('label', 'value', 'order')


@admin.register(Contact)
class ContactAdmin(SingletonModelAdmin, admin.ModelAdmin):
    fields = ('eyebrow_text', 'heading', 'description', 'map_embed_url', 'map_link', 'location_label')
    inlines = [ContactMethodInline]


@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'business_interest', 'is_read', 'created_at')
    list_filter = ('is_read', 'business_interest')
    search_fields = ('name', 'phone', 'email', 'message')
    readonly_fields = ('name', 'phone', 'email', 'business_interest', 'message', 'created_at')
    fields = ('name', 'phone', 'email', 'business_interest', 'message', 'is_read', 'created_at')
