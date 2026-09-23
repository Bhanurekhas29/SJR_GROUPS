from django.db import models


class Gallery(models.Model):
    """Singleton: Gallery section eyebrow and heading."""

    eyebrow_text = models.CharField(max_length=100, blank=True, default='Gallery')
    heading = models.TextField(help_text='e.g. A glimpse into our world.')

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Gallery Section'
        verbose_name_plural = 'Gallery Section'

    def __str__(self):
        return 'Gallery Section'

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass


class GalleryImage(models.Model):
    """One image, tagged with a category used for the filter tabs (e.g. Fashion Shelter)."""

    gallery = models.ForeignKey(Gallery, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='gallery/')
    category = models.CharField(max_length=100, help_text='e.g. Fashion Shelter, Sirippu Mittai, Om Muruga Ground')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.category} #{self.order}'
