from django.db import models


class FAQ(models.Model):
    """Singleton: FAQ section eyebrow and heading."""

    eyebrow_text = models.CharField(max_length=100, blank=True, default='Questions, Answered')
    heading = models.TextField(help_text='e.g. Everything you need to know.')

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'FAQ Section'
        verbose_name_plural = 'FAQ Section'

    def __str__(self):
        return 'FAQ Section'

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass


class FAQItem(models.Model):
    """One accordion question/answer pair."""

    faq = models.ForeignKey(FAQ, related_name='items', on_delete=models.CASCADE)
    question = models.CharField(max_length=255)
    answer = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.question
