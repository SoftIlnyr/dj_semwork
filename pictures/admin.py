from django.contrib import admin

# Register your models here.
from pictures.models import Picture


class PictureAdmin(admin.ModelAdmin):
    list_display = ["id", "artwork", "content", "description"]
    list_display_links = ["id"]
    search_fields = ["artwork"]

    class Meta:
        model = Picture


admin.site.register(Picture, PictureAdmin)
