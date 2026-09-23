from django.db import models


class Videos(models.Model):
    """Singleton: 'SJR Stories' section eyebrow and heading."""

    eyebrow_text = models.CharField(max_length=100, blank=True, default='SJR Stories')
    heading = models.TextField(help_text='e.g. See SJR Groups in motion.')

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Videos Section'
        verbose_name_plural = 'Videos Section'

    def __str__(self):
        return 'Videos Section'

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass


class VideoItem(models.Model):
    """One video, e.g. the large featured 'Our Story' video or a smaller list item."""

    videos = models.ForeignKey(Videos, related_name='items', on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to='videos/')
    label = models.CharField(max_length=100, help_text='e.g. Our Story, or Fashion Shelter')
    title = models.CharField(max_length=150, help_text='e.g. The world of SJR Groups')
    video_file = models.FileField(
        upload_to='videos/files/', blank=True, null=True,
        help_text='Upload the video file (mp4 recommended) to play it directly on the site',
    )
    video_url = models.URLField(
        blank=True, help_text='Used only if no video file is uploaded — a YouTube/Instagram link instead',
    )
    is_featured = models.BooleanField(default=False, help_text='Show as the large featured video')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title
