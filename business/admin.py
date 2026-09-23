from django.contrib import admin

from core.admin_base import SingletonModelAdmin
from .models import Business, BusinessItem


class BusinessItemInline(admin.StackedInline):
    model = BusinessItem
    extra = 4
    max_num = 4
    fields = (
        'image',
        'title',
        'tagline',
        'description',
        'features',
        'cta_text',
        'cta_link',
        'accent_color',
        'order',
    )


@admin.register(Business)
class BusinessAdmin(SingletonModelAdmin, admin.ModelAdmin):
    fields = ('eyebrow_text', 'heading')
    inlines = [BusinessItemInline]
