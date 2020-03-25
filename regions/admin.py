from django.contrib import admin

from regions.models import Town, Region


@admin.register(Region)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Town)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('name', 'region')
