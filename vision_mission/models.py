from django.db import models


class VisionMissionCard(models.Model):
    """One card, e.g. 'Our Vision' or 'Our Mission'."""

    label = models.CharField(max_length=100, help_text='e.g. Our Vision')
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Vision & Mission Card'
        ordering = ['order']

    def __str__(self):
        return self.label
