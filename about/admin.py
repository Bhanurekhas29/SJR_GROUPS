from django.contrib import admin

from core.admin_base import SingletonModelAdmin
from .models import About, AboutStat


class AboutStatInline(admin.TabularInline):
    model = AboutStat
    extra = 1
    fields = ('label', 'order')


@admin.register(About)
class AboutAdmin(SingletonModelAdmin, admin.ModelAdmin):
    fields = ('eyebrow_text', 'heading', 'description_primary', 'description_secondary')
    inlines = [AboutStatInline]
