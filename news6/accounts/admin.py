from django.contrib import admin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class AdminCustomForm(admin.ModelAdmin):
    form = CustomUserCreationForm
    add_form = CustomUserChangeForm
    model = CustomUser

    list_display =['username','email','age','is_staff',]

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age',)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('age',)}),
    )

admin.site.register(CustomUser, AdminCustomForm)