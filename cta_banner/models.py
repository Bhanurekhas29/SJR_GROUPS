from django.db import models


class CTABanner(models.Model):
    """Singleton: the dark 'Discover the world of SJR Groups' CTA banner."""

    eyebrow_text = models.CharField(max_length=150, blank=True, help_text='e.g. Fashion · Tradition · Fitness')
    heading = models.TextField(help_text='e.g. Discover the world of SJR Groups.')
    cta_text = models.CharField(max_length=50, blank=True, help_text='e.g. Explore Our Businesses')
    cta_link = models.CharField(max_length=255, blank=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'CTA Banner Section'
        verbose_name_plural = 'CTA Banner Section'

    def __str__(self):
        return 'CTA Banner Section'

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass
