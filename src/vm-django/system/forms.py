from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class CustomUserCreationForm(UserCreationForm):
    """
    User creation form (used in admin) for custom user model.
    """

    class Meta(UserCreationForm.Meta):
        model = User


class CustomUserChangeForm(UserChangeForm):
    """
    User info change form (used in admin) for custom user model.
    """

    class Meta(UserChangeForm.Meta):
        model = User
