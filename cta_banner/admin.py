from django.contrib import admin

from core.admin_base import SingletonModelAdmin
from .models import CTABanner


@admin.register(CTABanner)
class CTABannerAdmin(SingletonModelAdmin, admin.ModelAdmin):
    fields = ('eyebrow_text', 'heading', 'cta_text', 'cta_link')
