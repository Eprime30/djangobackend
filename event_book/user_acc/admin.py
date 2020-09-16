# Register your models here.
from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from .models import Account


class AccountAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email',
                    'username', 'phone', 'address', 'is_admin', 'is_staff', 'is_active')
    search_fields = ('email', 'username', 'last_name',)
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


# class EventAdmin(admin.ModelAdmin):
#     list_display = ('topic', 'time', 'venue',
#                     'room_capacity', 'speaker', 'tagline')
#     search_fields = ('topic', 'speaker', 'tagline')

#     filter_horizontal = ()
#     list_filter = ()
#     fieldsets = ()


admin.site.register(Account, AccountAdmin)
