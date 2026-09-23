from django.contrib import admin

from core.admin_base import SingletonModelAdmin
from .models import Social, SocialLink, SocialFeaturedCard


class SocialLinkInline(admin.TabularInline):
    model = SocialLink
    extra = 3
    fields = ('platform', 'url', 'order')


class SocialFeaturedCardInline(admin.TabularInline):
    model = SocialFeaturedCard
    extra = 4
    max_num = 4
    fields = ('thumbnail', 'label', 'link', 'order')


@admin.register(Social)
class SocialAdmin(SingletonModelAdmin, admin.ModelAdmin):
    fields = ('eyebrow_text', 'heading', 'description')
    inlines = [SocialLinkInline, SocialFeaturedCardInline]
