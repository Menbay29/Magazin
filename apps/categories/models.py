from django.db import models
from django.db.models.signals import pre_save


class Category(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Наименование'
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        related_name='children',
        null=True, blank=True
    )

    def __str__(self):
        return f"{self.title} -- {self.slug}"




