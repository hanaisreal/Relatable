from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models  import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'username']
    search_fields = ['username']

admin.site.register(User, UserAdmin)