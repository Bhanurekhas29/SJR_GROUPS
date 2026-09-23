from django.db import models


class Header(models.Model):
    """Singleton: site logo, brand name, tagline, and the header CTA button."""

    logo = models.ImageField(upload_to='header/', blank=True, null=True)
    brand_name = models.CharField(max_length=100, default='SJR GROUPS')
    tagline = models.CharField(max_length=150, blank=True)
    cta_text = models.CharField(max_length=50, blank=True, default='Connect With Us')
    cta_link = models.CharField(max_length=255, blank=True, default='#contact')
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Header & Navigation'
        verbose_name_plural = 'Header & Navigation'

    def __str__(self):
        return 'Header & Navigation'

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass


class NavigationItem(models.Model):
    header = models.ForeignKey(Header, related_name='nav_items', on_delete=models.CASCADE)
    label = models.CharField(max_length=50)
    link = models.CharField(max_length=255, help_text='URL or anchor, e.g. #about or /about/')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.label
