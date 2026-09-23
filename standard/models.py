from django.db import models


class Standard(models.Model):
    """Singleton: 'The SJR Standard' section eyebrow and heading."""

    eyebrow_text = models.CharField(max_length=100, blank=True, default='The SJR Standard')
    heading = models.TextField(help_text='e.g. More than businesses. A growing family.')

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'SJR Standard Section'
        verbose_name_plural = 'SJR Standard Section'

    def __str__(self):
        return 'SJR Standard Section'

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass


class StandardItem(models.Model):
    """One numbered value, e.g. '01 · Quality · Committed to delivering value.'"""

    standard = models.ForeignKey(Standard, related_name='items', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, help_text='e.g. Quality')
    description = models.CharField(max_length=200, blank=True, help_text='e.g. Committed to delivering value.')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title
