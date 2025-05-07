# --- form/models.py ---
from django.db import models
from django.utils.translation import gettext_lazy as _


class FormPage(models.Model):
    manifest = models.TextField(_('Manifest'), null=True)

    def __str__(self):
        return self.manifest or _('No manifest')