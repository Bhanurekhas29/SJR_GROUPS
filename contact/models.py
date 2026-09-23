from django.db import models


class Contact(models.Model):
    """Singleton: Contact section heading, description and map."""

    eyebrow_text = models.CharField(max_length=100, blank=True, default='Contact SJR Groups')
    heading = models.TextField(help_text="e.g. Let's connect.")
    description = models.TextField(blank=True)

    map_embed_url = models.URLField(blank=True, help_text='Google Maps embed URL')
    map_link = models.URLField(blank=True, help_text='"View on Google Maps" button link')
    location_label = models.CharField(max_length=100, blank=True, help_text='e.g. Kovilpatti')

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Contact Section'
        verbose_name_plural = 'Contact Section'

    def __str__(self):
        return 'Contact Section'

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass


class Enquiry(models.Model):
    """A submission from the enquiry form on the Contact section."""

    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    business_interest = models.CharField(max_length=150, blank=True, help_text='Selected business, e.g. Fashion Shelter')
    message = models.TextField(blank=True)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Enquiry'
        verbose_name_plural = 'Enquiries'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} ({self.created_at:%Y-%m-%d})'


class ContactMethod(models.Model):
    """One contact method, e.g. Call, WhatsApp, Email."""

    contact = models.ForeignKey(Contact, related_name='methods', on_delete=models.CASCADE)
    label = models.CharField(max_length=50, help_text='e.g. Call, WhatsApp, Email')
    value = models.CharField(max_length=255, help_text='e.g. Official number coming soon, or the actual number/email')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.label
