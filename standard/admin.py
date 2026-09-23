from django.contrib import admin

from core.admin_base import SingletonModelAdmin
from .models import Standard, StandardItem


class StandardItemInline(admin.TabularInline):
    model = StandardItem
    extra = 4
    max_num = 4
    fields = ('title', 'description', 'order')


@admin.register(Standard)
class StandardAdmin(SingletonModelAdmin, admin.ModelAdmin):
    fields = ('eyebrow_text', 'heading')
    inlines = [StandardItemInline]
