from django.db import models


class Footer(models.Model):
    """Singleton: footer logo/brand, description, connect details and copyright."""

    logo = models.ImageField(upload_to='footer/', blank=True, null=True)
    brand_name = models.CharField(max_length=100, blank=True, default='SJR GROUPS')
    tagline = models.CharField(max_length=150, blank=True, help_text='e.g. One Vision · Endless Possibilities')
    description = models.CharField(max_length=255, blank=True, help_text='e.g. One Group. Four Unique Businesses.')

    phone = models.CharField(max_length=50, blank=True, help_text='e.g. Coming soon')
    email = models.EmailField(blank=True)
    location = models.TextField(blank=True, help_text='Full address')

    copyright_text = models.CharField(max_length=150, blank=True, default='© 2026 SJR Groups. All Rights Reserved.')

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Footer Section'
        verbose_name_plural = 'Footer Section'

    def __str__(self):
        return 'Footer Section'

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass


class FooterLink(models.Model):
    """One link in either the 'Quick Links' or 'Our Businesses' footer column."""

    COLUMN_CHOICES = [
        ('quick_links', 'Quick Links'),
        ('businesses', 'Our Businesses'),
    ]

    footer = models.ForeignKey(Footer, related_name='links', on_delete=models.CASCADE)
    column = models.CharField(max_length=20, choices=COLUMN_CHOICES, default='quick_links')
    label = models.CharField(max_length=100)
    url = models.CharField(max_length=255, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['column', 'order']

    def __str__(self):
        return self.label


class FooterSocialLink(models.Model):
    """One social platform icon shown in the footer."""

    footer = models.ForeignKey(Footer, related_name='social_links', on_delete=models.CASCADE)
    platform = models.CharField(max_length=50, help_text='e.g. Facebook, Instagram, YouTube')
    url = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.platform
