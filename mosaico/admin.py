from django.contrib import admin

from .models import Upload, Template

admin.site.register(Upload)

@admin.register(Template)
class TemplateAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'created',
    ]
