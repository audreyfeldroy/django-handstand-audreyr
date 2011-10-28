from django.contrib import admin

from profiles.models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'fullname', 'email',)
    fields = ['user','username', 'fullname', 'email',]
    save_on_top = True
    search_fields = ['username', 'fullname', 'email',]

admin.site.register(Profile, ProfileAdmin)

