from django.contrib import admin

from .models import VisionMissionCard


@admin.register(VisionMissionCard)
class VisionMissionCardAdmin(admin.ModelAdmin):
    list_display = ('label', 'order')
    fields = ('label', 'description', 'order')
