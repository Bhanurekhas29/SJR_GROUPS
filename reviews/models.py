from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Reviews(models.Model):
    """Singleton: Reviews section eyebrow and heading."""

    eyebrow_text = models.CharField(max_length=100, blank=True, default='05 / Customer Stories')
    heading = models.TextField(help_text='e.g. What our customers say.')

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Reviews Section'
        verbose_name_plural = 'Reviews Section'

    def __str__(self):
        return 'Reviews Section'

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass


class Review(models.Model):
    """One customer testimonial shown in the carousel."""

    reviews = models.ForeignKey(Reviews, related_name='items', on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    business_location = models.CharField(max_length=150, blank=True, help_text='e.g. Business / Location')
    quote = models.TextField()
    rating = models.PositiveSmallIntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(5)])
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.customer_name
