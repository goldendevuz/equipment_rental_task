from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.shared.models import BaseModel
from apps.rental.models.category import Category


class Equipment(BaseModel):
    name = models.CharField(
        _("name"),
        max_length=100,
        help_text=_("Equipment name"),
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="equipments",
        help_text=_("Equipment category"),
    )
    daily_price = models.PositiveIntegerField(
        _("daily price"),
        help_text=_("Equipment daily price"),
    )
    status = models.BooleanField(
        _("status"),
        default=False,
        help_text=_("Equipment status"),
    )
    is_available = models.BooleanField(
        _("is available"),
        default=False,
        help_text=_("Equipment availability"),
    )
    rented = models.BooleanField(
        _("rented"),
        default=False,
        help_text=_("Equipment rented"),
    )
    in_maintenance = models.BooleanField(
        _("in maintenance"),
        default=False,
        help_text=_("Equipment in maintenance"),
    )
    is_lost = models.BooleanField(
        _("is lost"),
        default=False,
        help_text=_("Equipment lost"),
    )
    is_broken = models.BooleanField(
        _("is broken"),
        default=False,
        help_text=_("Equipment broken"),
    )
    image = models.ImageField(
        _("image"),
        upload_to="equipments/images/",
        help_text=_("Equipment image"),
        null=True,
        blank=True,
    )
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("equipment")
        verbose_name_plural = _("equipments")
