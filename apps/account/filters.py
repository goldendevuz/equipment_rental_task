from .models import User
from apps.shared.filters import make_filter

UserFilter = make_filter(User)
