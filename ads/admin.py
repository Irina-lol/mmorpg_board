from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Ad, Response, ConfirmationCode, User

@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category')
    list_filter = ('category',)
    search_fields = ('title', 'author__username')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "author":
            kwargs["queryset"] = User.objects.filter(is_active=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ('ad', 'author', 'text', 'is_accepted')

@admin.register(ConfirmationCode)
class ConfirmationCodeAdmin(admin.ModelAdmin):
    list_display = ('user', 'code', 'created_at')

admin.site.register(User, UserAdmin)
