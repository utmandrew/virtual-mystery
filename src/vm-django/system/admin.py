from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Group, Practical
from .forms import CustomUserChangeForm, CustomUserCreationForm


class CustomUserAdmin(UserAdmin):
    """
    Custom User Admin class.
    """
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('group', 'is_ta')}),
    )

    # fields to be displayed in admin
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('group', 'is_ta')}),
    )


# Register your models here.
admin.site.register(User, CustomUserAdmin)
admin.site.register(Group)
admin.site.register(Practical)
