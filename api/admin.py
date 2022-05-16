from django.contrib import admin

from api.models import Log


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display  = ('id', 'user', 'timestamp')
