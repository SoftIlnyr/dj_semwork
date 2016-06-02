from django.contrib import admin

# Register your models here.
from literature.models import Writing

class WritingAdmin(admin.ModelAdmin):
    list_display = ["id", "artwork", "description"]
    search_fields = ["content"]
    list_editable = ["description"]


    class Meta:
        model = Writing

admin.site.register(Writing, WritingAdmin)