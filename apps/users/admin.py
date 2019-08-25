from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from .models import User


class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (None, {
            'classes': (
                'wide',
            ),
            'fields': (
                'email',
                'password1',
                'password2',
            ),
        }),
    )
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': (
            'first_name',
            'last_name',
        )}),
        (_('Permissions'), {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
            ),
        }),
        (_('Important dates'), {'fields': (
            'last_login',
            'date_joined',
        )}),
    )
    filter_horizontal = (
        'groups',
        'user_permissions',
    )
    list_display = (
        'email',
        'avatar',
        'first_name',
        'last_name',
        'is_staff',
        'is_active',
    )
    list_filter = (
        'is_staff',
        'is_superuser',
        'is_active',
        'groups',
    )
    ordering = (
        'email',
    )
    search_fields = (
        'email',
        'first_name',
        'last_name',
    )


admin.site.register(User, UserAdmin)
