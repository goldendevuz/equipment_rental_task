from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.shared.models.base import BaseModel
from apps.shared.enums import UserRoles


class User(AbstractUser, BaseModel):
    """Custom User model with optional phone number and profile picture"""

    # Additional fields
    phone = models.CharField(
        _("phone number"),
        max_length=15,
        blank=True,
        null=True,
        help_text=_("Optional phone number"),
    )

    # Relationships
    groups = models.ManyToManyField(
        "auth.Group",
        verbose_name=_("groups"),
        blank=True,
        related_name="custom_user_set",
        related_query_name="custom_user",
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        verbose_name=_("user permissions"),
        blank=True,
        related_name="custom_user_set",
        related_query_name="custom_user",
    )

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self):
        return self.username
