from django.db import models


class About(models.Model):
    """Singleton: About section heading and the two description paragraphs."""

    eyebrow_text = models.CharField(max_length=100, blank=True, default='About SJR Groups')
    heading = models.TextField(help_text='Supports line breaks, e.g. "Building businesses.\\nCreating experiences."')
    description_primary = models.TextField(blank=True)
    description_secondary = models.TextField(blank=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'About Section'
        verbose_name_plural = 'About Section'

    def __str__(self):
        return 'About Section'

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass


class AboutStat(models.Model):
    """One numbered stat item, e.g. '01 · Four Businesses'. Number shown is its position."""

    about = models.ForeignKey(About, related_name='stats', on_delete=models.CASCADE)
    label = models.CharField(max_length=100, help_text='e.g. Four Businesses')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.label
