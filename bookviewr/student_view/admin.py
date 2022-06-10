from django.contrib import admin
from .models import Users, Books

from django.contrib.auth.admin import UserAdmin

# customizing the admin panel

class UserAdminConfig(UserAdmin):
    search_fields = ('email',)
    ordering = ('-email',)
    list_display = ('email','password','is_active','is_staff','is_superuser')

    # adding fields and making diffrent parts
    fieldsets = (
        (None, {'fields':('email','password')}),
        ('Permissions',{'fields':('is_staff','is_active', 'is_superuser')})
    )

    add_fieldsets = (
        (None,{
            'classes':('wide',),
            'fields':('email','password','is_staff','is_active')
        }),
    )
# Register your models here.
admin.site.register(Users, UserAdminConfig)
admin.site.register(Books)