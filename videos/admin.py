from django.contrib import admin

from core.admin_base import SingletonModelAdmin
from .models import Videos, VideoItem


class VideoItemInline(admin.StackedInline):
    model = VideoItem
    extra = 1
    fields = ('thumbnail', 'label', 'title', 'video_file', 'video_url', 'is_featured', 'order')


@admin.register(Videos)
class VideosAdmin(SingletonModelAdmin, admin.ModelAdmin):
    fields = ('eyebrow_text', 'heading')
    inlines = [VideoItemInline]
