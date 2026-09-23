from django.contrib import admin

from core.admin_base import SingletonModelAdmin
from .models import Reviews, Review


class ReviewInline(admin.StackedInline):
    model = Review
    extra = 1
    fields = ('customer_name', 'business_location', 'quote', 'rating', 'order')


@admin.register(Reviews)
class ReviewsAdmin(SingletonModelAdmin, admin.ModelAdmin):
    fields = ('eyebrow_text', 'heading')
    inlines = [ReviewInline]
