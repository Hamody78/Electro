from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

# Register your models here.

class AccountAdmin(UserAdmin): # هذا الكلاس تم انشائه لإضافة مميزات فى الصفحة الادمن وخاصةً فى الجدول الخاص بالمتسخدمين
    list_display = ("email", "first_name", "last_name", "username", "last_login", "date_joined", "is_active")

    list_display_links = ("email", "first_name", "last_name")

    readonly_fields = ("last_login", "date_joined")

    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)
