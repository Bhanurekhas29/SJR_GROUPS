from django.contrib import admin

from core.admin_base import SingletonModelAdmin
from .models import Gallery, GalleryImage


class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 1
    fields = ('image', 'category', 'order')


@admin.register(Gallery)
class GalleryAdmin(SingletonModelAdmin, admin.ModelAdmin):
    fields = ('eyebrow_text', 'heading')
    inlines = [GalleryImageInline]
