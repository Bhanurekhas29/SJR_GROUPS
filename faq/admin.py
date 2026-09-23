from django.contrib import admin

from core.admin_base import SingletonModelAdmin
from .models import FAQ, FAQItem


class FAQItemInline(admin.TabularInline):
    model = FAQItem
    extra = 1
    fields = ('question', 'answer', 'order')


@admin.register(FAQ)
class FAQAdmin(SingletonModelAdmin, admin.ModelAdmin):
    fields = ('eyebrow_text', 'heading')
    inlines = [FAQItemInline]
