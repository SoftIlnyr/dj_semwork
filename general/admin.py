from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from general.models import ArtWork, ArtUser, Comment


class ArtUserInLine(admin.StackedInline):
    model = ArtUser
    can_delete = False
    verbose_name_plural = "art_user"

class UserAdmin(BaseUserAdmin):
    inlines = (ArtUserInLine, )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

class ArtWorkAdmin(admin.ModelAdmin):
    list_display = ["id", "title",  "type", "pub_date", "rating"]
    list_editable = ["title"]
    search_fields = ["title", "type"]
    list_filter = ['type', "pub_date"]

    class Meta:
        model = ArtWork


admin.site.register(ArtWork, ArtWorkAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ["id","artwork", "publisher", "text", "pub_date"]
    list_filter = ["publisher", "pub_date"]
    search_fields = ["title", "text", "publisher"]

    class Meta:
        model = Comment

admin.site.register(Comment, CommentAdmin)
# admin.site.register(ArtUser)

