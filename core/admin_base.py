from django.shortcuts import redirect
from django.urls import reverse


class SingletonModelAdmin:
    """Mixin: forces a model down to one row and jumps straight to its change form.

    Used by every landing-page section app so each one appears as a single
    clickable item in the Jazzmin sidebar instead of a list/add screen.
    """

    def has_add_permission(self, request):
        return not self.model.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False

    def changelist_view(self, request, extra_context=None):
        obj, _ = self.model.objects.get_or_create(pk=1)
        opts = self.model._meta
        url = reverse('admin:%s_%s_change' % (opts.app_label, opts.model_name), args=[obj.pk])
        return redirect(url)
