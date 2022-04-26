from django.contrib import admin

from riding_sport_clubs.web_accounts.models import Profile, HorseUser


@admin.register(HorseUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'id',)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'user_id',)
    ordering = ('first_name', 'last_name', 'email',)
