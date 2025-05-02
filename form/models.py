from django.db import models

# Create your models here.

class FormPage(models.Model):
    manifest = models.TextField(null=True)

    def __str__(self):
        return self.manifest