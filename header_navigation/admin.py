from django.contrib import admin

from core.admin_base import SingletonModelAdmin
from .models import Header, NavigationItem


class NavigationItemInline(admin.TabularInline):
    model = NavigationItem
    extra = 1
    fields = ('label', 'link', 'order')


@admin.register(Header)
class HeaderAdmin(SingletonModelAdmin, admin.ModelAdmin):
    fields = ('logo', 'brand_name', 'tagline', 'cta_text', 'cta_link')
    inlines = [NavigationItemInline]
