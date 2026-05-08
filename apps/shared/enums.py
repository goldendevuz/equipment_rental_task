from django.db import models
from django.utils.translation import gettext_lazy as _
from icecream import ic


class UserRoles(models.TextChoices):
    ORDINARY_USER = "ordinary_user", _("Ordinary User")
    CUSTOMER = "customer", _("Customer")
    ADMIN = "admin", _("Admin")
    SUPER_ADMIN = "super_admin", _("Super Admin")

    def __str__(self):
        return str(self.label)


class RentalStatuses(models.TextChoices):
    ACTIVE = "active", _("Active")
    INACTIVE = "inactive", _("Inactive")
    RETURNED = "returned", _("Returned")
    LATE_RETURNED = "late_returned", _("Late Returned")
    LOST = "lost", _("Lost")
    BROKEN = "broken", _("Broken")

    def __str__(self):
        return str(self.label)
