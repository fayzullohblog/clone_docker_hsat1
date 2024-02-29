# from django.contrib import admin
# from .models import MyUser
# # Register your models here.

# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.forms import UserChangeForm,UserCreationForm
# from .models import MyUser
# from .forms import MyUserChangeForm,MyUserCreationForm


# class MyUserAdmin(admin.ModelAdmin):
#     model = MyUser
#     list_display = ['username', 'phone_number', 'user_number_litter', 'role_user', 'state']

# admin.site.register(MyUser, MyUserAdmin)

from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserChangeForm,UserCreationForm
from .models import MyUser
from django.contrib.auth.backends import ModelBackend

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm
    


    list_display = ['username','is_superuser','is_staff','is_active','is_boss']
    list_filter = ["is_staff"]

    fieldsets = [
        (None, {"fields": ["password",'username',]}),
        ("Personal info", {"fields": ["first_name",'last_name','phone_number','user_number_litter','party_name']}),
        ("Permissions", {"fields": ['is_active','is_superuser','is_staff','is_boss']}),
    ]
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["username", "password1", "password2",'is_active','image'],
            },
        ),
    ]
    search_fields = ["user_number_litter"]
    ordering = ["user_number_litter"]
    filter_horizontal = []
    list_editable=['is_staff','is_active','is_superuser','is_boss']



    def _allow_edit(self, obj=None):
        if not obj:
            return True
        return  (obj.is_superuser or obj.is_active)

    def has_change_permission(self, request, obj=None):
        return self._allow_edit(obj)

    def has_delete_permission(self, request, obj=None):
        return self._allow_edit(obj)

    def has_add_permission(self, request):
        return True

    def has_view_permission(self, request, obj=None):
        return True

    def has_module_permission(self, request):
        return True


# Now register the new UserAdmin...
admin.site.register(MyUser, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)
