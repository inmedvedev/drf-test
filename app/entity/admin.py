from django.contrib import admin

from .models import Property, Entity


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    pass


@admin.register(Entity)
class EntityAdmin(admin.ModelAdmin):
    pass
