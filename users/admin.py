from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'avatar', 'first_name', 'last_name', 'verification_key', 'is_verified')
    search_fields = ('email',)
