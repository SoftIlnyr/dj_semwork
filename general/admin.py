from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from general.models import ArtWork, ArtUser


class ArtUserInLine(admin.StackedInline):
    model = ArtUser
    can_delete = False
    verbose_name_plural = "art_user"

class UserAdmin(BaseUserAdmin):
    inlines = (ArtUserInLine, )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(ArtWork)
# admin.site.register(ArtUser)

