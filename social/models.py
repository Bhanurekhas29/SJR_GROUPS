from django.db import models


class Social(models.Model):
    """Singleton: 'Stay Connected' section eyebrow, heading and description."""

    eyebrow_text = models.CharField(max_length=100, blank=True, default='Stay Connected')
    heading = models.TextField(help_text='e.g. Follow the SJR Groups journey.')
    description = models.TextField(
        blank=True,
        default='Official social channels will be connected here once supplied by the SJR Groups team.',
    )

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Stay Connected Section'
        verbose_name_plural = 'Stay Connected Section'

    def __str__(self):
        return 'Stay Connected Section'

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass


class SocialLink(models.Model):
    """One social platform icon, e.g. Facebook, Instagram, YouTube."""

    social = models.ForeignKey(Social, related_name='links', on_delete=models.CASCADE)
    platform = models.CharField(max_length=50, help_text='e.g. Facebook, Instagram, YouTube')
    url = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.platform


class SocialFeaturedCard(models.Model):
    """One brand thumbnail card, e.g. Fashion Shelter's latest video/post."""

    social = models.ForeignKey(Social, related_name='featured_cards', on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to='social/')
    label = models.CharField(max_length=100, help_text='e.g. Fashion Shelter')
    link = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.label
