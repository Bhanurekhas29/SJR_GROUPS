from django.db import models


class Hero(models.Model):
    """Singleton: hero badge, heading, description, and the two CTA buttons."""

    badge_text = models.CharField(max_length=150, blank=True, help_text='e.g. One Vision · Four Businesses · Endless Possibilities')
    heading = models.TextField(help_text='Supports line breaks, e.g. "One group.\\nFour unique businesses."')
    description = models.TextField(blank=True)

    primary_cta_text = models.CharField(max_length=50, blank=True)
    primary_cta_link = models.CharField(max_length=255, blank=True)

    secondary_cta_text = models.CharField(max_length=50, blank=True)
    secondary_cta_link = models.CharField(max_length=255, blank=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Hero Section'
        verbose_name_plural = 'Hero Section'

    def __str__(self):
        return 'Hero Section'

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass


class HeroSlide(models.Model):
    """One background carousel image. Frontend auto-plays through these with no indicators."""

    hero = models.ForeignKey(Hero, related_name='slides', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='hero/')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'Slide {self.order}'
