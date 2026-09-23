from django.db import models


class Business(models.Model):
    """Singleton: the 'Our Businesses' intro eyebrow and heading."""

    eyebrow_text = models.CharField(max_length=100, blank=True, default='Our Businesses')
    heading = models.TextField(help_text='e.g. Four brands. One identity.')

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Businesses Section'
        verbose_name_plural = 'Businesses Section'

    def __str__(self):
        return 'Businesses Section'

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass


class BusinessItem(models.Model):
    """One brand card, e.g. 'Fashion Shelter / Covering Jewellery'."""

    business = models.ForeignKey(Business, related_name='items', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='business/')
    title = models.CharField(max_length=150, help_text='e.g. Fashion Shelter / Covering Jewellery')
    tagline = models.CharField(max_length=150, blank=True, help_text='e.g. Style That Shines.')
    description = models.TextField(blank=True)
    features = models.TextField(blank=True, help_text='One feature per line, e.g. Trendy Collections')
    cta_text = models.CharField(max_length=50, blank=True, help_text='e.g. Explore on Fashion Shelter')
    cta_link = models.CharField(max_length=255, blank=True)
    accent_color = models.CharField(max_length=20, blank=True, help_text='Hex color for this brand, e.g. #8B5E34')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

    def feature_list(self):
        return [line.strip() for line in self.features.splitlines() if line.strip()]
