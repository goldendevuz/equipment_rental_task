from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.shared.models import BaseModel


class Category(BaseModel):
    name = models.CharField(
        _("name"),
        max_length=100,
        help_text=_("Category name"),
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")
