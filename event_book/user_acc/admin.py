from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user_acc.models import Account
# Register your models here.


class AccountAdmin(UserAdmin):
    list_display = ('first_name', 'last_name', 'email',
                    'username', 'phone', 'address', 'is_admin', 'is_staff', 'is_active')
    search_fields = ('email', 'username', 'last_name',)
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)
