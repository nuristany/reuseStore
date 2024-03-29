
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
# Register your models here.

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'contact_number', 'is_staff', 'is_active')
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2", "email", "contact_number", "first_name", "last_name"),
            },
        ),
    )



# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from .models import User

# from shop.models import UserProfile

# class UserProfileInline(admin.StackedInline):
#     model = UserProfile
#     can_delete = False

# @admin.register(User)
# class UserAdmin(BaseUserAdmin):
#     inlines = (UserProfileInline,)
#     list_display = ('username', 'email', 'is_staff', 'is_active')

#     # Modify add_fieldsets to include contact_number from UserProfile
#     add_fieldsets = (
#         (
#             None,
#             {
#                 "classes": ("wide",),
#                 "fields": ("username", "password1", "password2", "email", "contact_number", "first_name", "last_name"),
#             },
#         ),
#     )



    