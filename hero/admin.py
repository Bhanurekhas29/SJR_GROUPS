from django.contrib import admin

from core.admin_base import SingletonModelAdmin
from .models import Hero, HeroSlide


class HeroSlideInline(admin.TabularInline):
    model = HeroSlide
    extra = 1
    fields = ('image', 'order')


@admin.register(Hero)
class HeroAdmin(SingletonModelAdmin, admin.ModelAdmin):
    fields = (
        'badge_text',
        'heading',
        'description',
        'primary_cta_text',
        'primary_cta_link',
        'secondary_cta_text',
        'secondary_cta_link',
    )
    inlines = [HeroSlideInline]
