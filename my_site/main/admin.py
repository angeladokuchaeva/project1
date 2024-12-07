from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from main.models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # Настраиваем отображение в списке
    list_display = ('user_id', 'username', 'is_active')
    search_fields = ('username',)
    ordering = ('date_joined',)

    # Настраиваем формы редактирования
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'is_staff', 'is_active'),
        }),
    )
