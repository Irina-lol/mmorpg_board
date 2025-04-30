from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Ad, Response, ConfirmationCode, User

class AdAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category')
    list_filter = ('author', 'category')
    search_fields = ('title', 'author__username')
    raw_id_fields = ['author']

admin.site.register(Ad, AdAdmin)
admin.site.register(Response)
admin.site.register(ConfirmationCode)
admin.site.register(User, UserAdmin)
