from django.contrib import admin
from userauths.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email', 'bio']


admin.site.register(User, UserAdmin)
