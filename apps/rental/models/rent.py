from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.shared.models import BaseModel
from apps.rental.models.equipment import Equipment
from apps.shared.enums import RentalStatuses


class Rent(BaseModel):
    client_name = models.CharField(
        _("client name"),
        max_length=100,
        help_text=_("Client name"),
    )
    client_phone = models.CharField(
        _("client phone"),
        max_length=15,
        help_text=_("Client phone"),
    )
    equipment = models.ForeignKey(
        Equipment,
        on_delete=models.CASCADE,
        related_name="rents",
        help_text=_("Rented equipment"),
    )
    start_date = models.DateField(
        _("start date"),
        help_text=_("Rent start date"),
    )
    end_date = models.DateField(
        _("end date"),
        help_text=_("Rent end date"),
    )
    total_price = models.DecimalField(
        _("total price"),
        max_digits=10,
        decimal_places=2,
        help_text=_("Rent total price"),
    )
    rental_status = models.CharField(
        _("rental status"),
        max_length=20,
        choices=RentalStatuses,
        default="pending",
        help_text=_("Rental status"),
    )

    def __str__(self):
        return self.client_name

    class Meta:
        verbose_name = _("rent")
        verbose_name_plural = _("rents")
