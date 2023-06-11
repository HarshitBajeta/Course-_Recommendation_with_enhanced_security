from django.contrib import admin
from .models import Order, Order_Item, Userimage, User, UserManager
from django.contrib.auth.admin import UserAdmin


# Register your models here.
admin.site.register(Order)
admin.site.register(Order_Item)
admin.site.register(Userimage)

    
    
class CustomUserAdmin(UserAdmin):
    # Specify the fields to display in the admin interface
    list_display = ['username', 'email','hashed_password','password','is_active', 'is_staff', 'is_superuser']

    # Specify the fields to filter on in the admin interface
    list_filter = ['is_active', 'is_staff', 'is_superuser']

    # Specify the fields to search on in the admin interface
    search_fields = ['username', 'email']

    # Specify the fieldsets for the add and change forms in the admin interface
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )

    # Specify the add and change forms for the admin interface
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )

admin.site.register(User, CustomUserAdmin)

# admin.site.register(User, CustomUserAdmin)